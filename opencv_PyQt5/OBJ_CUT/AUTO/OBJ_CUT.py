#НАХОДИТ НА КАРТИНКАХ С БЕЛЫМ ФОНОМ ОДНОЦВЕТНЫЕ ОБЪЕКТЫ, ВЫРЕЗАЕТ ИХ В ОТДЕЛЬНЫЕ КАРТИНКИ С НАЗВАНИЯМИ=КООРДИНАТАМИ РАСПОЛОЖЕНИЯ НА КАРТИНКЕ-ИСХОДНИКЕ
#появл-ся в папке 1/objects


#добавить необх число картинок до-после, при необходимости пропустить ненужные, обрезать любую из них, вырезать с картинок или названия или объекты, если названия, то белый прямоуг с черн каймой после, если объект то вырезать чтобы цвет фона


import cv2, pickle, os, numpy as np
from operator import itemgetter, attrgetter, methodcaller

#path0 = os.getcwd() #All=os.listdir() #path = path0 + '/' + str(Qnr)
path = '1'
os.chdir(path)


img = cv2.imread('1.jpg')
Ymax,Xmax = 600, 1000
img=img[0:Ymax,0:Xmax]
img2=img #print(img[300,160])
S =img.shape #print(S)
ys,xs = img.shape[0], img.shape[1]

#cv2.FloodFill( img, CvPoint(100,100), CvScalar( color = CV_BGR(100, 100, 100) ) )

#'''
# созд-е и сохр-е массива сvet со всеми тчк нечерн, небел, несер

cvet, ObjNach, ObjKon = [], [], []

shag = 10 # norm 16 1 10
lvll = 3
razmax = 15

#print(ys, ys/shag, ys//shag, xs, xs/shag, xs//shag)

i, j = 1, 1
bgrBlack, bgrWhite = list(range(11)), list(range(240,256))
while j <= ys//shag-1:
	while i <= xs//shag-1:

		if True:
			y,x = shag*j, shag*i
			if j%2 == 0:
				x += shag//2
			B, G, R = img[y][x][0], img[y][x][1], img[y][x][2]
			#print(j,y,i,x,img[y][x])
			B_min1, G_min1, R_min1 = img[y][x-shag][0] , img[y][x-shag][1] , img[y][x-shag][2]
			nearB_min1, nearG_min1, nearR_min1 = list(range(B_min1-20,B_min1+20)) , list(range(G_min1-20,G_min1+20)) , list(range(R_min1-20,R_min1+20))
			
			isgrey = B == G == R
			isgrey_min1 = B_min1 == G_min1 == R_min1

			isblack = B in bgrBlack and G in bgrBlack and R in bgrBlack
			isblack_min1 = B_min1 in bgrBlack and G_min1 in bgrBlack and R_min1 in bgrBlack
			
			iswhite = B in bgrWhite and G in bgrWhite and R in bgrWhite
			iswhite_min1 = B_min1 in bgrWhite and G_min1 in bgrWhite and R in bgrWhite

			issamecolor = B in nearB_min1 and G in nearG_min1 and R in nearR_min1

		if (isgrey) or (isblack) or (iswhite):

			
			if (not (isgrey_min1)) and (not (isblack_min1)) and (not (iswhite_min1)):

				ObjKon.append([y,x,img[y][x][0],img[y][x][1],img[y][x][2]])
	
		else:

			cvet.append([y,x,img[y][x][0],img[y][x][1],img[y][x][2]])
			
		i += 1
	
	j += 1
	i = 1

razmax1 = 10
SR = [115, 28, 126]
SRB,SRG,SRR = list(range((SR[0]-razmax1),(SR[0]+razmax1))), list(range((SR[1]-razmax1),(SR[1]+razmax1))), list(range((SR[2]-razmax1),(SR[2]+razmax1)))
# a in list == min(list) <= a <= max(list)
print('cvet is made. cvet[0] = ', cvet[0])

cvet2=[]
for i in cvet:
	cvet2.append([i[2], i[3], i[4]]) #, i[0],i[1]])

print('len(cvet2) = ',len(cvet2), '. cvet2[0] =',cvet2[0])

#for i in cvet2: ##print('SR in cvet2')
	#if i[0] in SRB and i[1] in SRG and i[2] in SRR:
		#print('SR in cvet2')

tchk = []
i=0
while i<len(cvet2):
	a = cvet2.count(cvet2[i])
	if a > lvll:
		tchk.append([cvet[i][2], cvet[i][3], cvet[i][4], cvet[i][0], cvet[i][1]]) 
	i += 1
print('tchk',len(tchk), 'tchk[0] = ', tchk[0])

tchki = sorted(tchk, key=itemgetter(0)) #= sorted(cvet, key=itemgetter(2,3,4))

#for i in tchki: #print('SR in tchki')
	#if i[0] in SRB and i[1] in SRG and i[2] in SRR:
		#print('SR in tchki')

colors2 = tchki

cvet3 = sorted(colors2, key=itemgetter(2))
t = 1
while True:
	now, prev = cvet3[t], cvet3[t-1]
	B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
	#print(cvet3[t],cvet3[t-1],cvet3[t][1],[(cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax)])
	if now[0] in B and now[1] in G and now[2] in R:
		cvet3.remove(cvet3[t])
		#print('remove')
	else:
		t += 1
		#print('t+1')

	if t == len(cvet3):
		break


#for i in cvet3: #print('SR in cvet3')
	#if i[0] in SRB and i[1] in SRG and i[2] in SRR:
		#print('SR in cvet3')

cvet3 = sorted(cvet3, key=itemgetter(1))
t = 1
while True:
	now, prev = cvet3[t], cvet3[t-1]
	B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
	#print(cvet3[t],cvet3[t-1],cvet3[t][1],[(cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax)])
	if now[0] in B and now[1] in G and now[2] in R:
		cvet3.remove(cvet3[t])
		#print('remove')
	else:
		t += 1
		#print('t+1')

	if t == len(cvet3):
		break
print('len(cvet3) = ', len(cvet3))

cvet3 = sorted(cvet3, key=itemgetter(0))
t = 1
while True:
	now, prev = cvet3[t], cvet3[t-1]
	B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
	#print(now,prev, 'b',min(B), max(B), 'g', min(G),max(G), 'r', min(R), max(R))
	if now[0] in B and now[1] in G and now[2] in R:
		cvet3.remove(cvet3[t])
		#print('remove')
	else:
		t += 1
		#print('t+1')

	if t == len(cvet3):
		break
print('len(cvet3) = ', len(cvet3))
#'''

'''
	cvet3 = sorted(cvet3, key=itemgetter(1))
	t = 1
	while True:
		now, prev = cvet3[t], cvet3[t-1]
		B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
		#print(cvet3[t],cvet3[t-1],cvet3[t][1],[(cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax)])
		if now[0] in B and now[1] in G and now[2] in R:
			cvet3.remove(cvet3[t])
			#print('remove')
		else:
			t += 1
			#print('t+1')

		if t == len(cvet3):
			break
	print(len(cvet3))

	cvet3 = sorted(cvet3, key=itemgetter(3))
	t = 1
	while True:
		now, prev = cvet3[t], cvet3[t-1]
		B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
		#print(cvet3[t],cvet3[t-1],cvet3[t][1],[(cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax)])
		if now[0] in B and now[1] in G and now[2] in R:
			cvet3.remove(cvet3[t])
			#print('remove')
		else:
			t += 1
			#print('t+1')

		if t == len(cvet3):
			break
	print(len(cvet3))

	cvet3 = sorted(cvet3, key=itemgetter(4))
	t = 1
	while True:
		now, prev = cvet3[t], cvet3[t-1]
		B,G,R = list(range((cvet3[t-1][0]-razmax),(cvet3[t-1][0]+razmax))), list(range((cvet3[t-1][1]-razmax),(cvet3[t-1][1]+razmax))), list(range((cvet3[t-1][2]-razmax),(cvet3[t-1][2]+razmax)))
		print(now, 'b',min(B), max(B), 'g', min(G),max(G), 'r', min(R), max(R))
		if now[0] in B and now[1] in G and now[2] in R:
			cvet3.remove(cvet3[t])
			print('remove')
		else:
			t += 1
			print('t+1')

		if t == len(cvet3):
			break
	print(len(cvet3))
	'''

#'''
for i in cvet3:
	cv2.circle(img2, (i[4], i[3]), 5, (0,0,0), -1)

cvet3 = sorted(cvet3, key=itemgetter(4))

print('cvet3',cvet3)

razmax2 = 20
cvet4=[]
for m in cvet3:
	#print(i)
	#yx = []
	ymin,ymax,xmin,xmax = m[3],m[3],m[4],m[4]
	B,G,R,_,_ = m
	b,g,r = 0,0,0
	count = 0
	for i in cvet:
		if B - razmax2 <= i[2] <= B + razmax2:
			if G - razmax2 <= i[3] <= G + razmax2:
				if R - razmax2 <= i[4] <= R + razmax2:
					#yx.append([i[0],i[1]])
					ymin = min(ymin,i[0])
					ymax = max(ymax,i[0])
					xmin = min(xmin,i[1])
					xmax = max(xmax,i[1])
					b += i[2]
					g += i[3]
					r += i[4]
					count += 1

	ymin -= shag
	ymax += shag
	xmin -= shag
	xmax += shag
	cvet4.append([b//count,g//count,r//count,ymin,ymax,xmin,xmax])

print('cvet4[5]',cvet4[5])

#with open('cvet4.pickle', 'wb') as f:
#	pickle.dump(cvet4, f)
#'''
#'''
#with open('cvet4.pickle', 'rb') as f:
#	cvet4 = pickle.load(f)
#'''
#'''

objnr = 0
while objnr< len(cvet4):
	print('objnr', objnr)
	BB, GG, RR, ymin, ymax, xmin, xmax = cvet4[objnr]
	if ymin == 0 or xmin == 0 or ymax == Ymax or xmax == Xmax:
		objnr += 1
		continue
	
	razmax3=15

	#созд+сохр массива obj с тчкми нашего объекта (по цветовому диапазону
	#obj=np.zeros((ymax-ymin,xmax-xmin,3), dtype=np.uint8)
	#obj2=np.zeros((ymax-ymin,xmax-xmin,4), dtype=np.uint8)
	obj=np.zeros((Ymax,Xmax,3), dtype=np.uint8)
	obj2=np.zeros((Ymax,Xmax,4), dtype=np.uint8)
	b=list(range(BB-razmax3,BB+razmax3))
	g=list(range(GG-razmax3,GG+razmax3))
	r=list(range(RR-razmax3,RR+razmax3))

	y, x = ymin, xmin
	while y < ymax:
		while x < xmax:
			#print(img[y,x],img[y,x,0], img[y,x,0] in b)
			if img[y,x,0] in b and img[y,x,1] in g and img[y,x,2] in r:
				obj2[y,x] = np.append(img[y,x], 255)
				obj[y,x] = img[y,x]
				#img2[y,x] = np.array((255,255,255))
				#print(obj[y-ymin,x-xmin])
			x += 1
		y += 1
		x = xmin

	hsv = cv2.cvtColor( obj, cv2.COLOR_BGR2HSV ) 
	hsv_min = np.array((1, 0, 0), np.uint8)
	hsv_max = np.array((254, 255, 255), np.uint8)
	thresh = cv2.inRange( hsv, hsv_min, hsv_max )

	contours, hierarchy = cv2.findContours( thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for i in contours:
		area = cv2.contourArea(i)
		if area>60:
			x,y,w,h = cv2.boundingRect(i)
			obj = obj2[y:(y+h),x:(x+w)]
			name = 'objects/obj' + str(objnr) + '_x' + str(x) + 'y' + str(y) + 'w' + str(w) + 'h' + str(h) + '.png'
			print(name, 'area =', area)
			cv2.imwrite(name,obj)
			x -= 2
			y -= 2
			w += 4
			h += 4
			#extcontours = np.array([[x,y],[x,y+h],[x+w,y+h],[x+w,y]])
			#cv2.fillPoly(img2, pts =[extcontours], color=(255,255,255))
	#cv2.drawContours( img, contours, -1, (255,255,255), cv2.FILLED, cv2.LINE_AA, hierarchy, 1)


	objnr += 1

#a = contours, hierarchy, thresh
#with open('contours.pickle', 'wb') as f:
#	pickle.dump(a, f)


#cv2.drawContours( obj, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )

#cv2.imwrite('objects/obj2.png',obj)


''' как делать вырез по нормальному
	# BGR, uint8(0-255), программой Digital Color Meter
	low_red = (100,150,120)
	high_red = (140,190,160)
	only = cv2.inRange(img, low_red, high_red)

	moments = cv2.moments(only, 1)
	dM01 = moments['m01']
	#print(dM01)
	dM10 = moments['m10']
	#print(dM10)
	dArea = moments['m00']
	#print(dArea)
	# будем реагировать только на те моменты,
	# которые содержать больше 100 пикселей
	if dArea > 100:
	    x = int(dM10 / dArea)
	    y = int(dM01 / dArea)
	    cv2.circle(img, (x, y), 10, (0,0,255), -1)
	    '''


cv2.namedWindow("Scaled image", cv2.WINDOW_NORMAL) # create a resizeable window
cv2.imshow("Scaled image", img2) # display the image in the window
cv2.resizeWindow("Scaled image", 800, 600) # resize the window

#cv2.namedWindow("Scaledimage", cv2.WINDOW_NORMAL) # create a resizeable window
#cv2.imshow("Scaledimage", obj) # display the image in the window
#cv2.resizeWindow("Scaledimage", 800, 600)

cv2.waitKey(0)
