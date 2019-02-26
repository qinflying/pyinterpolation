#!/usr/bin/python3
#-*- coding:utf-8 -*-
import sys

def Run():
	from PyQt5.QtWidgets import QApplication, QWidget
	from PyQt5.QtCore import QCoreApplication
	print("test")

	app = QApplication(sys.argv)


	from dialog import mainmenu
	oMainMenu = mainmenu.CMainUI()
	oMainMenu.show()

	sys.exit(app.exec_())

def Ui2Py():
	import ui2pytool
	ui2pytool.Run()

if __name__ == "__main__":
	iLen = len(sys.argv)
	if iLen >= 2:
		sCmd = sys.argv[1]
		if sCmd == '1':
			Run()
		elif sCmd == '9':
			Ui2Py()
	else:
		Run()