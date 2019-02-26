#!/usr/bin/python3
#-*- coding:utf-8 -*-

from uicode import mainui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QIcon
from PyQt5.QtCore import Qt, QTimer

FRAME_CNT = 30 
DRAW_SPEED = 200

class CMainUI(mainui.Ui_Form, QWidget):
	DRAW_EDGE_X = 10 
	DRAW_EDGE_Y = 10
	DRAW_W = 760
	DRAW_H = 620
	DRAW_RECT = (DRAW_EDGE_X, DRAW_EDGE_Y, DRAW_W, DRAW_H)
	POINT_SIZE = 10
	DRAW_CENTER_X = DRAW_EDGE_Y + DRAW_W/2
	DRAW_CENTER_Y = DRAW_EDGE_Y + DRAW_H/2
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
		self.m_Timer = None
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
		self.m_Calc = lagrange.Lagrange(self.m_MapPoints[:])
		self.AwakeDraw()

	def AwakeDraw(self):
		self.m_IsDrawLine = True
		self.m_CurX = 0
		self.m_AccTime = 0
		self.m_Lines = []

		self.m_Timer = QTimer(self)
		self.m_Timer.timeout.connect(self.onLoopDraw)
		self.m_Timer.start(1000/FRAME_CNT)

	def onNewton(self):
		print("onNewton")
		from algorithms import newton
		self.m_Calc = newton.Newton(self.m_MapPoints[:])
		self.AwakeDraw()

	def onHermite(self):
		print("onHermite")
		from algorithms import hermite
		self.m_Calc = hermite.NormalHermite(self.m_MapPoints[:])
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
			x, y = self.view2drawpos(x, y)
			self.m_MapPoints.append((x, y))
			print (x, y)
			self.update()

	def isContainer(self, x, y):
		x1, y1, x2, y2 = self.DRAW_EDGE_X, self.DRAW_EDGE_Y, self.DRAW_EDGE_X + self.DRAW_W, self.DRAW_H + self.DRAW_EDGE_Y
		if x <= x1 or x >= x2:
			return False 
		if y <= y1 or y >= y2:
			return False
		return True

	def view2drawpos(self, vx, vy):
		x = vx - self.DRAW_CENTER_X
		y = self.DRAW_CENTER_Y - vy 
		return x, y 

	def draw2viewpos(self, dx, dy):
		x = self.DRAW_CENTER_X + dx 
		y = self.DRAW_CENTER_Y - dy
		return x, y

	def drawCoordinate(self, qp):
		lXCoordinate = [self.DRAW_EDGE_X, self.DRAW_CENTER_Y,  + self.DRAW_EDGE_X + self.DRAW_W, self.DRAW_CENTER_Y]
		lYCoordinate = [self.DRAW_CENTER_X, self.DRAW_EDGE_Y, self.DRAW_CENTER_X, self.DRAW_EDGE_Y + self.DRAW_H]
		pen = QPen(QColor(0, 0, 0), 1)
		qp.setPen(pen)
		for lRect in (lXCoordinate,lYCoordinate):
			x1, y1, x2, y2 = lRect
			qp.drawLine(x1, y1, x2, y2)

		lText = []

		x = self.DRAW_CENTER_X
		y = self.DRAW_CENTER_Y
		lPos = [(x, y)]
		
		lText.append((x-10, y+10, 0))
		#正x
		v = 100
		while x + v < self.DRAW_EDGE_X + self.DRAW_W:
			lText.append((x+v-10, y+10, v))
			lPos.append((x+v, y))
			v += 100
		v = -100
		#负x
		while x + v > self.DRAW_EDGE_X: 
			lText.append((x+v-10, y+10, v))
			lPos.append((x+v, y))
			v -= 100

		#正y
		v = -100 
		while y + v > self.DRAW_EDGE_Y:
			lText.append((x-22, y+v+3, -v))
			lPos.append((x, y+v))
			v -= 100 

		#负y
		v = 100
		while y + v < self.DRAW_EDGE_Y + self.DRAW_H:
			lText.append((x-25, y+v+3, -v))
			lPos.append((x, y+v))
			v += 100

		pen = QPen(QColor(0, 0, 0), 2)
		qp.setPen(pen)
		for x, y in lPos:
			qp.drawPoint(x, y)

		pen = QPen(QColor(0, 0, 0), 1)
		qp.setPen(pen)
		for x, y, v in lText:
			s = "%d" % v 
			qp.drawText(x, y, s)

	def drawInterpolation(self, qp):
		lPoints = self.m_Points[:]
		lPoints.sort(key=lambda a:a[0])

		bgColor = QColor(255, 255, 255)
		qp.setBrush(bgColor)
		qp.drawRect(*self.DRAW_RECT)

		self.drawCoordinate(qp)

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
		self.m_AccTime += 1.0 / FRAME_CNT * DRAW_SPEED
		if self.m_AccTime >= self.DRAW_RECT[2]:
			if self.m_Timer:
				self.m_Timer.stop()
				self.m_Timer = None
		x = self.m_AccTime
		x = -self.DRAW_W/2 + x
		y = self.m_Calc(x)
		x, y = self.draw2viewpos(x, y)
		self.m_Lines.append((x, y))
		self.update()


