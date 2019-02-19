#!/usr/bin/python3
#-*- coding:utf-8 -*-

from uicode import mainui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QIcon
from PyQt5.QtCore import Qt, QTimer

FRAME_CNT = 30 

class CMainUI(mainui.Ui_Form, QWidget):
	DRAW_RECT = (10, 10, 760, 620)
	POINT_SIZE = 10
	def __init__(self):
		mainui.Ui_Form.__init__(self)
		QWidget.__init__(self)
		self.m_Points = []
		self.m_MapPoints = []
		self.m_Lines = []
		self.m_CurX = 0
		self.m_DrawPanel = None
		self.m_IsDrawLine = False
		self.m_AccTime = 0
		self.m_Calc = None
		self.setupUi(self)

	def setupUi(self, From):
		mainui.Ui_Form.setupUi(self, From)
		#图标
		self.setWindowIcon(QIcon("resources/icons/logo.png"))
		#不拉伸
		self.setFixedSize(self.width(), self.height())

	def onLagrange(self):
		print("onLagrange")
		from algorithms import lagrange
		self.m_Calc = lagrange.Lagrange
		self.AwakeDraw()



	def AwakeDraw(self):
		self.m_IsDrawLine = True
		self.m_CurX = 0
		self.m_AccTime = 0

		self.m_Timer = QTimer(self)
		self.m_Timer.timeout.connect(self.onLoopDraw)
		self.m_Timer.start(1000/FRAME_CNT)

	def onNewton(self):
		print("onNewton")
		from algorithms import newton
		self.m_Calc = newton.Newton
		self.AwakeDraw()
		
	def onClearDraw(self):
		print("onClearDraw")
		self.m_Points = []
		self.m_Lines = []
		self.m_MapPoints = []
		self.m_CurX = 0 
		self.m_IsDrawLine = False
		if self.m_Timer:
			self.m_Timer.stop()
			self.m_Timer = None
		self.update()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawInterpolation(qp)
		qp.end()

	def mousePressEvent(self, event):
		if self.m_IsDrawLine:
			return
		if event.button() == Qt.LeftButton:
			point = event.pos()
			x, y = point.x(), point.y()
			if not self.isContainer(x, y):
				return
			self.m_Points.append((x, y))
			self.m_MapPoints.append((x, 640 - y))
			print (x, 640 -y)
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

		iLen = len(self.m_Lines)


		if iLen >= 2:
			pen = QPen(QColor(0, 255, 255), 2)
			qp.setPen(pen)
			for i in range(iLen-1):
				startx, starty = self.m_Lines[i]
				endx, endy = self.m_Lines[i+1]
				qp.drawLine(startx, starty, endx, endy)

	def onLoopDraw(self):
		if not self.m_IsDrawLine:
			return
		self.m_AccTime += 1.0 / FRAME_CNT * 100
		if self.m_AccTime >= self.DRAW_RECT[2]:
			self.m_Timer.stop()
			self.m_Timer = None
		x = self.m_AccTime
		y = self.m_Calc(self.m_MapPoints, x)
		self.m_Lines.append((x, 640 - y))
		self.update()


