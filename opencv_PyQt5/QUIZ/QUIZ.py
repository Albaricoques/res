#решить проблему со вторым появлением интерактивного вопроса, на текущий момент он не появляется
#если не идет как правильно скроллбар - увеличь число '\n' в Story
#ЕСЛИ НЕ РБОТЕТ КЛАВИАТУРА В ИНТЕРКТИВАХ - textEdit.releaseKeyboard() перед переходом к интерактиву
import random, sys, os
from PyQt5 import QtWidgets, QtCore, QtGui

with open('questions.txt') as Q: 
    txt=list(Q.readlines())
    lengthQ=len(txt)
txtQnrs=[str(i) for i in range(lengthQ)]
#print(txtQnrs)

#поиск интерктивных вопросов
InteractiveQnrs=[]
All=os.listdir()
for i in All:
    if i[2].isdigit():
        InteractiveQnrs.append(i)
#print(InteractiveQnrs)

allQnrs = txtQnrs + InteractiveQnrs
#решить проблему со вторым появлением интерактивного вопроса, на текущий момент он не появляется
#allQnrs = InteractiveQnrs

#print(allQnrs)

path0 = os.getcwd()

Q=['','','',''] #Q = Qnr,z,V,O
class randomizer: 
	def step(spisokvoprosov): #__колл__?
		Qnr=random.choice(spisokvoprosov)
		#Qnr='i130'
		z=Qnr[0]

		#пересылка по z соответствующему классу выполнения
		global Q
		if z.isdigit():
			Question=txt[int(Qnr)].split('?')
			V='> ' + Question[0] + '?'
			O='Правильный ответ: ' + Question[1]
			#return Qnr,z,V,O, Question
			
			Q = Qnr,z,V,O
			Vopros.setText(Q[2])
			LabelRightAnsIs.setText(Q[3])

		else:
			path = path0 + '/' + str(Qnr)
			os.chdir(path)
			Ins=os.listdir()
			for i in Ins:
				if i[-4:] == '.png' and i[0:2] != 'bg':
					V = str(i[:-4])
			O = path + '/' + V + '.png'
			
			Q = Qnr,z,V,O
			import pyqt8
			pyqt8.w1.accepted.connect(Interreaction.ans)
#на закрытие пикт8 добвить в скроллбр Q[2] и Q[3] и продолжить цикл - по сигналу!!
class Interreaction:
	def ans():
		global Story, L
		Story += '\n\n' + '> ' + Q[2] + '\n' + '>> <a href="file://' + Q[3] + '">link</a>'
		History=QtWidgets.QLabel(Story)
		History.setWordWrap(True)
		History.setOpenExternalLinks(True)
		scrollarea.setWidget(History)
		L=scrollarea.widget().height()
		scrollarea.ensureVisible(0,L)
		randomizer.step(allQnrs)


app = QtWidgets.QApplication(sys.argv)

Story=30*'\n'	
L = 0	

class b1(QtWidgets.QPushButton):
	def __init__(self, title):
		super().__init__(title)
	def mousePressEvent(self,e):
		QtWidgets.QPushButton.mousePressEvent(self,e)
		if e.button() == QtCore.Qt.LeftButton:
			LabelRightAnsIs.show()
			LabelWereYouRight.show()
			button3.show()
			button4.setChecked(False)
			button4.show()
			scrollarea.ensureVisible(0,L)
			#emit Visible(true)
			textEdit.releaseKeyboard()
			button3.setFocus()

	def obrab():
		LabelRightAnsIs.show()
		LabelWereYouRight.show()
		button3.show()
		button4.setChecked(False)
		button4.show()
		scrollarea.ensureVisible(0,L)
		#emit Visible(true)
		textEdit.releaseKeyboard()
		button3.setFocus()

class b3(QtWidgets.QPushButton):
	def __init__(self, title):
		super().__init__(title)
		
	def keyPressEvent(self, event):
		#print("pressed key " + str(event.key()))
		if event.key() == 32:
			b4.obrab()
		elif event.key() == 16777220:
			b3.obrab()

	def mousePressEvent(self, e):
		QtWidgets.QPushButton.mousePressEvent(self, e)
		if e.button() == QtCore.Qt.LeftButton:
			global Story, L
			Story += '\n\n' + Q[2] + '\n' + '>> ' + textEdit.text()
			History=QtWidgets.QLabel(Story)
			History.setWordWrap(True)
			History.setOpenExternalLinks(True)
			scrollarea.setWidget(History)
			L=scrollarea.widget().height()
			scrollarea.ensureVisible(0,L)
			textEdit.clear()
			
			#Vopros.setText(Q[2])
			#LabelRightAnsIs.setText(Q[3])
			LabelRightAnsIs.hide()
			LabelWereYouRight.hide()
			
			button4.setChecked(True)
			button3.hide()
			button4.hide()

			textEdit.grabKeyboard()
			textEdit.setFocus()
			#emit Visible(false)
			randomizer.step(allQnrs)

	def obrab():
		global Story, L
		Story += '\n\n' + Q[2] + '\n' + '>> ' + textEdit.text()
		History=QtWidgets.QLabel(Story)
		History.setWordWrap(True)
		History.setOpenExternalLinks(True)
		scrollarea.setWidget(History)
		L=scrollarea.widget().height()
		scrollarea.ensureVisible(0,L)
		textEdit.clear()

		LabelRightAnsIs.hide()
		LabelWereYouRight.hide()

		button4.setChecked(True)
		button3.hide()
		button4.hide()
		#emit Visible(false)
		textEdit.grabKeyboard()
		textEdit.setFocus()

		randomizer.step(allQnrs)
		#Vopros.setText(Q[2])
		#LabelRightAnsIs.setText(Q[3])
		
class b4(QtWidgets.QPushButton):
	def __init__(self, title):
		super().__init__(title)
		self.setCheckable(True)

	def mousePressEvent(self, e):
		QtWidgets.QPushButton.mousePressEvent(self, e)
		if e.button() == QtCore.Qt.LeftButton:
			textEdit.clear()
			LabelRightAnsIs.hide()
			LabelWereYouRight.hide()

			button4.setChecked(True)
			button3.hide()
			button4.hide()
			#emit Visible(false)
			textEdit.grabKeyboard()
			textEdit.setFocus()

	def obrab():
		textEdit.clear()
		LabelRightAnsIs.hide()
		LabelWereYouRight.hide()

		button4.setChecked(True)
		button3.hide()
		button4.hide()
		textEdit.grabKeyboard()
		textEdit.setFocus()

class MainWindow(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Quiz')
		self.resize(800,500)


scrollarea = QtWidgets.QScrollArea()

History=QtWidgets.QLabel(Story)
History.setWordWrap(True)
History.setOpenExternalLinks(True)
scrollarea.setWidget(History)
L=scrollarea.widget().height()
scrollarea.ensureVisible(0,L)


textEdit = QtWidgets.QLineEdit()
textEdit.grabKeyboard()
textEdit.returnPressed.connect(b1.obrab)
hbox = QtWidgets.QHBoxLayout()
button1 = b1('Send (Enter)')
hbox.addWidget(button1)
LabelWereYouRight = QtWidgets.QLabel('Вы ответили правильно?')
hbox2 = QtWidgets.QHBoxLayout()
button3 = b3('I was right (Enter)')
button4 = b4(' &No:( Try again! (Space)')
button4.setChecked(True)

hbox2.addWidget(button4)
hbox2.addWidget(button3)
Vopros = QtWidgets.QLabel(Q[2])
Vopros.setWordWrap(True)
LabelRightAnsIs = QtWidgets.QLabel(Q[3])
LabelRightAnsIs.setWordWrap(True)

form = QtWidgets.QFormLayout()#form.setRowWrapPolicy( wrapAllRows)
form.addRow(scrollarea)
form.addRow(Vopros)# - здесь мжн что то нчльное
form.addRow(textEdit)
form.addRow(hbox)
form.addRow(LabelRightAnsIs)
form.addRow(LabelWereYouRight)
form.addRow(hbox2)

LabelRightAnsIs.hide()
LabelWereYouRight.hide()
button3.hide()
button4.hide()

randomizer.step(allQnrs)

w=MainWindow()
w.setLayout(form)
w.show()

sys.exit(app.exec_())