from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from time_convert import Ui_MainWindow
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def convert_12():
	hour = ui.hour_12.value()
	mint = ui.mint_12.value()
	if 0 <= hour <= 23 and 0 <= mint <= 59:
		if 0 <= mint <= 9:
			mint = '0'+str(mint)
		if 1 <= hour <= 11:
			ui.screen_12.setText(str(hour)+':'+str(mint)+' am')
		elif 13 <= hour <= 23:
			hour -= 12
			ui.screen_12.setText(str(hour)+':'+str(mint)+' pm')
		elif hour == 0:
			ui.screen_12.setText('12:'+str(mint)+' am')
		elif hour == 12:
			ui.screen_12.setText('12:'+str(mint)+' pm')
	else:
		ui.screen_12.setText('TIME IS WRONG !')

def convert_24():
	hour = ui.hour_24.value()
	mint = ui.mint_24.value()
	am = ui.am.isChecked()
	pm = ui.pm.isChecked()
	if (am == True) and (1 <= hour <= 12 and 0 <= mint <= 59):
		if 1 <= hour <= 11:
			ui.screen_24.setText(str(hour)+':'+str(mint))
		elif hour == 12:
			ui.screen_24.setText('00:'+str(mint))
	elif (pm == True) and (1 <= hour <= 12 and 0 <= mint <= 59):
		if 1 <= hour <= 11:
			hour += 12
			ui.screen_24.setText(str(hour)+':'+str(mint))
		elif hour == 12:
			ui.screen_24.setText(str(hour)+':'+str(mint))
	else:
		ui.screen_24.setText('TIME IS WRONG !')

ui.convert_12.clicked.connect(convert_12)
ui.convert_24.clicked.connect(convert_24)

sys.exit(app.exec_())