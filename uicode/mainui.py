# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/uifiles\mainui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 640)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(790, 0, 161, 631))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(5, 15, 5, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.m_LagrangeBtn = QtWidgets.QPushButton(self.widget)
        self.m_LagrangeBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_LagrangeBtn.setObjectName("m_LagrangeBtn")
        self.verticalLayout.addWidget(self.m_LagrangeBtn)
        self.m_NewtonBtn = QtWidgets.QPushButton(self.widget)
        self.m_NewtonBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_NewtonBtn.setObjectName("m_NewtonBtn")
        self.verticalLayout.addWidget(self.m_NewtonBtn)
        spacerItem = QtWidgets.QSpacerItem(148, 506, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.m_ClearBtn = QtWidgets.QPushButton(self.widget)
        self.m_ClearBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_ClearBtn.setObjectName("m_ClearBtn")
        self.verticalLayout.addWidget(self.m_ClearBtn)
        self.m_LagrangeBtn.raise_()
        self.m_ClearBtn.raise_()

        self.retranslateUi(Form)
        self.m_LagrangeBtn.clicked.connect(Form.onLagrange)
        self.m_ClearBtn.clicked.connect(Form.onClearDraw)
        self.m_NewtonBtn.clicked.connect(Form.onNewton)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "插值与拟合演示"))
        self.m_LagrangeBtn.setText(_translate("Form", "拉格朗日插值算法"))
        self.m_NewtonBtn.setText(_translate("Form", "牛顿插值算法"))
        self.m_ClearBtn.setText(_translate("Form", "清除"))

