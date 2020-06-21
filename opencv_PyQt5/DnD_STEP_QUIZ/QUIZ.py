import os, pickle,sys
from PyQt5 import QtWidgets, QtCore, QtGui
#pickle для сохрнения мест дропа

background = 'bg.png'

'''
path0 = os.getcwd()
Question='i130'
path = path0 + '/' + str(Question)
os.chdir(path)
'''

Ins=os.listdir()
for i in Ins:
    if i[-4:] == '.png' and i[0:2] != 'bg':
        endimage = str(i)
#print(endimage)

ourimage1=os.listdir('objects')
n = len(ourimage1)

a=open('pos.pickle','rb')
Pos=pickle.load(a)

dic = {} #в последнем виджете здесь будут пары адресов драг-дроп
isdone=0
done=0
# скрывать оригиналы в нчле перенос и удлять при првильном рзмещении, чтобы была только одна копия рисунка в рбочем прострнстве ИЛИ СКРОЛЛ БАР!!

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

        global dic, isdone #,score

        if event.mimeData().hasImage() and dic[event.source()] == self:
            dropped = QtGui.QPixmap(event.mimeData().imageData())
            self.setPixmap(dropped)
            dic[event.source()] = '0'


            for i in dic:
                if str(dic[i]).isdigit() == False:
                    isdone+=1
            if isdone==0:
                #score+=1
                #print('Your score is ', score)
                w2.exec_()
            else:
                isdone=0

class CloseLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            w2.accept()
            w1.accept()
            done=1

#QDialog!!!!
class window(QtWidgets.QDialog):
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
        global dic
        qwpix, label, c, d, label_to_drag = [],[],[],[],[]
        ourimage=[]
        for i in range(n):
            ourimage.append('objects/'+ourimage1[i])
            qwpix.append(QtGui.QPixmap(ourimage[i]))
            c.append(qwpix[i].width())
            d.append(qwpix[i].height())
            label_to_drag.append(DraggableLabel(self, ourimage[i]))
 #           print(label_to_drag[i])
            label_to_drag[i].setGeometry(0,sum(d[0:i]),c[i],d[i])

            if Pos.get(ourimage[i]) != None :
                label.append(DropLabel('', self))
                label[len(label)-1].setGeometry(Pos[ourimage[i]][0]-c[i]/2, Pos[ourimage[i]][1]-d[i]/2, c[i], d[i]) 
                dic[label_to_drag[i]] = label[len(label)-1]
            else:
                dic[label_to_drag[i]] = '0'

        self.show()

class window2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        wpixmap = QtGui.QPixmap(endimage)
        windowwidth = wpixmap.width()
        windowheight = wpixmap.height()
        self.setWindowTitle('Done!')
        self.resize(windowwidth,windowheight) 
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(wpixmap))
        pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(wpixmap)) 
        self.setPalette(pal) 
        
        Closelabel=CloseLabel('', self)
        Closelabel.setGeometry(0,0,windowwidth,windowheight)
        #Congrats='Поздравляем!'+'\n'+'Вы правильно ответили на вопрос и получаете еще 1 балл!'+'\n'+'Правильный ответ выглядит так:'+'\n'+'(для продолжения щелкните правой кнопкой мыши)' #СДЕЛТЬ РЗНЫЙ ШРИФТ И ПРО ПРОДОЛЖЕ СЕРЫМ
        #self.accepted.connect(self.close())

#УБРАТЬ АППЫ ПЕРЕД УСТНОВКОЙ В ОБЩИЙ ПОТОК
app = QtWidgets.QApplication(sys.argv)

w1 = window()
w2 = window2()
w1.show()

sys.exit(app.exec_())