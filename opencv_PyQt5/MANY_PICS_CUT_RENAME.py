#обрезать по данным координатам x0 x y0 y копии всех картинок в заданной папке и, переименовав, закинуть в другую папку

x0,x, y0, y = 0, 717, 50, 486
source_dir = 'spanish/'
result_dir = 'SpLang/'

result_template = result_dir + 's{}.png'

#which symbols (number of order) are borders of info to save from names of source_files
#for example "some_stuff_USEFUL_INFORMATIONNN_somestuff" U - 11, N - 30
s1, s2 = 11, 30
#cuts for these borders and places only useful info into new name

import cv2, os
All=os.listdir(source_dir)

for i in All:
	#print(i)
	img = cv2.imread(source_dir + i)
	img = img[y0:y,x0:x]
	name = result_template.format(i[s1:s2])
	cv2.imwrite(name, img)


'''
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''