# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Dec 23 23:35:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.leftVtk = QVTKRenderWindowInteractor(Form)
        self.leftVtk.setObjectName(_fromUtf8("leftVtk"))
        self.verticalLayout.addWidget(self.leftVtk)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.rightVtk = QVTKRenderWindowInteractor(Form)
        self.rightVtk.setObjectName(_fromUtf8("rightVtk"))
        self.verticalLayout_2.addWidget(self.rightVtk)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.okienkowanieTab = QtGui.QWidget()
        self.okienkowanieTab.setObjectName(_fromUtf8("okienkowanieTab"))
        self.tabWidget.addTab(self.okienkowanieTab, _fromUtf8(""))
        self.cannyTab = QtGui.QWidget()
        self.cannyTab.setObjectName(_fromUtf8("cannyTab"))
        self.tabWidget.addTab(self.cannyTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.loadImage = QtGui.QPushButton(Form)
        self.loadImage.setObjectName(_fromUtf8("loadImage"))
        self.verticalLayout_3.addWidget(self.loadImage)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Oryginalny obraz", None))
        self.label_2.setText(_translate("Form", "Przetworzony obraz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.okienkowanieTab), _translate("Form", "Okienkowanie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cannyTab), _translate("Form", "Canny", None))
        self.loadImage.setText(_translate("Form", "Wczytaj obraz", None))

from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
