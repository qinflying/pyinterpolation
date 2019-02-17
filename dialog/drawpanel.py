#!/usr/bin/python3
#-*- coding:utf-8 -*-

from uicode import drawpanel as drawpanelui
from PyQt5.QtWidgets import QWidget


class CDrawPanel(drawpanelui.Ui_Form, QWidget):
	def __init__(self, parent):
		drawpanelui.Ui_Form.__init__(self)
		QWidget.__init__(self)

		self.setupUi(self)

	def setupUi(self, From):
		drawpanelui.Ui_Form(self, From)

		

