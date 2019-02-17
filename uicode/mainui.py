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
        self.m_LagrangeBtn = QtWidgets.QPushButton(Form)
        self.m_LagrangeBtn.setGeometry(QtCore.QRect(790, 10, 161, 41))
        self.m_LagrangeBtn.setObjectName("m_LagrangeBtn")
        self.m_ClearBtn = QtWidgets.QPushButton(Form)
        self.m_ClearBtn.setGeometry(QtCore.QRect(790, 590, 161, 41))
        self.m_ClearBtn.setObjectName("m_ClearBtn")

        self.retranslateUi(Form)
        self.m_LagrangeBtn.clicked.connect(Form.onLagrange)
        self.m_ClearBtn.clicked.connect(Form.onClearDraw)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.m_LagrangeBtn.setText(_translate("Form", "拉格朗日插值算法"))
        self.m_ClearBtn.setText(_translate("Form", "清除"))

