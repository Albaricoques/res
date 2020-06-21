score = 10

background="premrnaE.png"
ourimage = ['bbp.png', 'u1.png', 'u2af.png', 'u2.png', 'u4u5u6.png']
n = len(ourimage)
endimage='premrnaEfinal.png'

a = [462, 262, 521]
b = 205
#координаты места дропа заносить в словрь по изобржению, которое туда надо дропнуть
now = 0
fin = len(a)

dic = {} #в последнем виджете здесь будут пары адресов драг-дроп
isdone=0
# скрывать оригиналы в нчле перенос и удлять при првильном рзмещении, чтобы была только одна копия рисунка в рбочем прострнстве

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
'''
class PlaceLabel(QtWidgets.QLabel):
    def __init__(self, parent): 
        super(QtWidgets.QLabel, self).__init__(parent) 
    def mousePressEvent(self,event):
        print(event.pos())
'''
class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, parent, image): 
        super(QtWidgets.QLabel, self).__init__(parent) 
        self.setPixmap(QtGui.QPixmap(image)) 
    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.pos()
    def mouseMoveEvent(self, event):
        data = QtCore.QMimeData()
        data.setImageData(self.pixmap().toImage()) 
        drag = QtGui.QDrag(self)
        drag.setMimeData(data) 
        drag.setPixmap(self.pixmap()) 
        drag.setHotSpot(event.pos())
        act = drag.exec_(QtCore.Qt.MoveAction)

class DropLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs) 
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event): 
        if event.mimeData().hasImage(): 
            event.accept() 
        else:
            event.ignore()
    def dropEvent(self, event):
        global dic
        if event.mimeData().hasImage() and dic[event.source()] == self:
            dropped = QtGui.QPixmap(event.mimeData().imageData())
            self.setPixmap(dropped)

            dic[event.source()] = '0'
#            print(dic)
            global isdone
            for i in dic:
                if str(dic[i]).isdigit() == False:
                    isdone+=1
 #               print(isdone)
 #       global isdone
            if isdone==0:
                print("Вы справились! Вы набрали ",score," очков.")
                quit()
            else:
                isdone=0



class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        wpixmap = QtGui.QPixmap(background)
        windowwidth = wpixmap.width()
        windowheight = wpixmap.height()
        self.setWindowTitle('Quiz')
        self.resize(windowwidth,windowheight) 
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(wpixmap))
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(wpixmap)) 
        self.setPalette(pal) 

        self.initUI()

    def initUI(self):
        qwpix, label, c, d, label_to_drag = [],[],[],[],[]
        for i in range(n):
            qwpix.append(QtGui.QPixmap(ourimage[i]))
            c.append(qwpix[i].width())
            d.append(qwpix[i].height())
            label_to_drag.append(DraggableLabel(self, ourimage[i]))
 #           print(label_to_drag[i])
            label_to_drag[i].setGeometry(0,sum(d[0:i]),c[i],d[i]) 
        global dic

        for i in range(fin):
            label.append(DropLabel('', self))#, label_to_drag[i])) 
            label[i].setGeometry(a[i]-c[i]/2,b-d[i]/2,c[i],d[i])
            dic[label_to_drag[i]] = label[i]
        for i in range(fin,n):
            dic[label_to_drag[i]] = '0'


        '''
        labelplace=PlaceLabel(self)
        wpixmap = QtGui.QPixmap(background)
        windowwidth = wpixmap.width()
        windowheight = wpixmap.height()
        labelplace.setGeometry(0,0,windowwidth,windowheight)
        '''

        self.show()


app = QtWidgets.QApplication(sys.argv)
w=window()
w.show() 
sys.exit(app.exec_())


