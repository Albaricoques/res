#вырезать все азоты, кислороды, они же со связями с кольцом, водородные связи, номера углеродов. сохранить позицию объекта в названии. очернобелить, чтобы все кружочки стали серого цвета, а все связи вырезать с картинки

import cv2
import numpy as np

xy = []

# mouse callback function
def onMouseImage(event,x,y,flags,param):

    global xy, objBGR #, objHSV

    if event == cv2.EVENT_MOUSEMOVE:

        img2 = img.copy()

        if xy != []:
            cv2.line(img2, (0,xy[1]), (Xmax,xy[1]), (0,0,0), 2);  #crosshair horizontal
            cv2.line(img2, (xy[0],0),(xy[0],Ymax), (0,0,0), 2);  #crosshair vertical
            #print(xy)
            if len(xy) >= 4:
                cv2.line(img2, (0,xy[3]), (Xmax,xy[3]), (0,0,0), 2);  #crosshair horizontal
                cv2.line(img2, (xy[2],0),(xy[2],Ymax), (0,0,0), 2);  #crosshair vertical
                #print(xy)

        cv2.line(img2, (0,y), (Xmax,y), (0,0,0), 1);  #crosshair horizontal
        cv2.line(img2, (x,0),(x,Ymax), (0,0,0), 1);  #crosshair vertical
        
        cv2.imshow('image',img2)


    elif event == cv2.EVENT_LBUTTONDOWN:
        xy.append(x)
        xy.append(y)

    elif event == cv2.EVENT_LBUTTONUP:

        if y - xy[1] < 5 and x - xy[0] < 5:
            return

        xy.append(x)
        xy.append(y)

        objBGR = img[xy[1]:y,xy[0]:x].copy()
        #objHSV = cv2.cvtColor(objBGR, cv2.COLOR_BGR2HSV) 
        
        cv2.rectangle(img, (xy[0],xy[1]), (xy[2],xy[3]), (255,255,255), -1)
        template = 'obj_{}_{}.png'
        xxx, yyy = str((xy[0] + xy[1])/2), str((xy[2]+xy[3])/2)
        name = template.format(xxx, yyy)
        cv2.imwrite(name, objBGR) #obj2


#        cv2.namedWindow('obj')
#        cv2.imshow('obj',objBGR)
#        cv2.setMouseCallback('obj', onMouseObject)
#        #cv2.imwrite('obj.png',obj)
#        cv2.waitKey()
#        cv2.destroyWindow('obj')
        xy = []

def onMouseObject(event,x,y,flags,param):


    if event == cv2.EVENT_LBUTTONDOWN:
        
        Range = 20 
        
        #colors = objHSV[y,x]
        B,G,R = objBGR[y,x]
        #colorsmin = [i - Range for i in colors]
        #colorsmax = [i + Range for i in colors]

        ymax = objBGR.shape[0]
        xmax = objBGR.shape[1]

        print(ymax, xmax)

        b=list(range(B-Range,B+Range))
        g=list(range(G-Range,G+Range))
        r=list(range(R-Range,R+Range))

        obj2=np.zeros((ymax,xmax,4), dtype=np.uint8)

        yA, xA = 0, 0
        while yA < ymax:
            while xA < xmax:
                #print(img[y,x],img[y,x,0], img[y,x,0] in b)
                if objBGR[yA,xA,0] in b and objBGR[yA,xA,1] in g and objBGR[yA,xA,2] in r:
                    obj2[yA,xA] = np.append(objBGR[yA,xA], 255)
                    #obj[y,x] = img[y,x]
                    #img2[y,x] = np.array((255,255,255))
                    #print(obj[y-ymin,x-xmin])
                xA += 1
            yA += 1
            xA = 0
            #print(yA)

        cv2.imwrite('obj.png', obj2)
        print('Done')



        #print(colorsmin, colorsmax)
'''
        #hsv = cv2.cvtColor(obj, cv2.COLOR_BGR2HSV) 
        hsv_min = np.array(colorsmin, np.uint8)
        print(hsv_min)
        hsv_max = np.array(colorsmax, np.uint8)
        thresh = cv2.inRange(objHSV, hsv_min, hsv_max)

        contours, hierarchy = cv2.findContours( thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        number = 1
        for i in contours:
            
            area = cv2.contourArea(i)
            print(area)
            if area>60:
                x2,y2,w,h = cv2.boundingRect(i)
                obj = obj2[y2:(y2+h),x2:(x2+w)]
                #        name = 'obj.png'
                #        #name = 'objects/obj' + str(objnr) + '_x' + str(x) + 'y' + str(y) + 'w' + str(w) + 'h' + str(h) + '.png'
                #        print(name, 'area =', area)
                cv2.imwrite(str(number) + '.png', obj)
            number += 1
        #        x -= 2
        #        y -= 2
        #        w += 4
        #        h += 4
'''


# Create an image, a window and bind the function to window
img = cv2.imread('1.png')
Ymax,Xmax = 600, 1000
#img=img[0:Ymax,0:Xmax].copy()
#img3 = img.copy()

S =img.shape #print(S)
ys,xs = img.shape[0], img.shape[1]
print(S,ys,xs)

cv2.namedWindow('image')
cv2.setMouseCallback('image',onMouseImage)

cv2.imshow('image',img)
cv2.waitKey()
