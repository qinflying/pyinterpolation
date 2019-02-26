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
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(790, 0, 161, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(5, 15, 5, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.m_LagrangeBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.m_LagrangeBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_LagrangeBtn.setObjectName("m_LagrangeBtn")
        self.verticalLayout.addWidget(self.m_LagrangeBtn)
        self.m_NewtonBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.m_NewtonBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_NewtonBtn.setObjectName("m_NewtonBtn")
        self.verticalLayout.addWidget(self.m_NewtonBtn)
        self.m_HermiteBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.m_HermiteBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.m_HermiteBtn.setObjectName("m_HermiteBtn")
        self.verticalLayout.addWidget(self.m_HermiteBtn)
        spacerItem = QtWidgets.QSpacerItem(148, 506, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.m_ClearBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.m_ClearBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.m_ClearBtn.setObjectName("m_ClearBtn")
        self.verticalLayout.addWidget(self.m_ClearBtn)

        self.retranslateUi(Form)
        self.m_LagrangeBtn.clicked.connect(Form.onLagrange)
        self.m_ClearBtn.clicked.connect(Form.onClearDraw)
        self.m_NewtonBtn.clicked.connect(Form.onNewton)
        self.m_HermiteBtn.clicked.connect(Form.onHermite)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "插值与拟合演示"))
        self.m_LagrangeBtn.setText(_translate("Form", "拉格朗日插值(Lagrange)"))
        self.m_NewtonBtn.setText(_translate("Form", "牛顿插值(Newton)"))
        self.m_HermiteBtn.setText(_translate("Form", "埃尔米特插值(Hermite)"))
        self.m_ClearBtn.setText(_translate("Form", "清除"))

