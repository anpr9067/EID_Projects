from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import TouchScreen
import sensorui

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)

	while True:
		print("Enter Type of UI")
		print("1. TouchScreen")
		print("2. Simple")
		choice = input("Enter here:")
		print(choice)
		if(int(choice) ==1 or int(choice)==2):
			break
		else:
			print("Try Again")
			continue
	if(int(choice) == 1):
	    Form = QtWidgets.QWidget()
	    ui = TouchScreen.Ui_Form()
	    ui.setupUi(Form)
	    Form.show()
	    sys.exit(app.exec_())
	elif(int(choice) == 2):
		    MainWindow = QtWidgets.QMainWindow()
		    ui = sensorui.Ui_MainWindow()
		    ui.setupUi(MainWindow)
		    MainWindow.show()
		    sys.exit(app.exec_())
