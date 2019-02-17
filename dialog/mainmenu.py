#!/usr/bin/python3
#-*- coding:utf-8 -*-

from uicode import mainui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt

class CMainUI(mainui.Ui_Form, QWidget):
	DRAW_RECT = (10, 10, 760, 620)
	POINT_SIZE = 10
	def __init__(self):
		mainui.Ui_Form.__init__(self)
		QWidget.__init__(self)
		self.setupUi(self)
		self.m_Points = []

	def onLagrange(self):
		print("onLagrange")
		
	def onClearDraw(self):
		print("onClearDraw")
		self.m_Points = []
		self.update()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawInterpolation(qp)
		qp.end()

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			point = event.pos()
			x, y = point.x(), point.y()
			if not self.isContainer(x, y):
				return
			self.m_Points.append((x, y))
			self.update()

	def isContainer(self, x, y):
		xx, yy, w, h = self.DRAW_RECT
		if x <= xx or x >= xx + w:
			return False 
		if y <= yy or y >= yy + h:
			return False
		return True

	def drawInterpolation(self, qp):
		lPoints = self.m_Points[:]
		lPoints.sort(key=lambda a:a[0])

		bgColor = QColor(255, 255, 255)
		qp.setBrush(bgColor)
		qp.drawRect(*self.DRAW_RECT)

		pen = QPen(Qt.red, 5)

		qp.setPen(pen)
		for point in lPoints:
			qp.drawPoint(*point)


