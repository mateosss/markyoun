# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created: Mon May 12 19:44:47 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(251, 284)
        Menu.setMinimumSize(QtCore.QSize(251, 284))
        Menu.setMaximumSize(QtCore.QSize(251, 284))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Menu.setWindowIcon(icon)
        Menu.setAutoFillBackground(False)
        self.nuevo = QtGui.QPushButton(Menu)
        self.nuevo.setGeometry(QtCore.QRect(10, 70, 231, 61))
        self.nuevo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nuevo.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Nuevo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nuevo.setIcon(icon1)
        self.nuevo.setCheckable(False)
        self.nuevo.setFlat(False)
        self.nuevo.setObjectName(_fromUtf8("nuevo"))
        self.abrir = QtGui.QPushButton(Menu)
        self.abrir.setGeometry(QtCore.QRect(10, 140, 231, 61))
        self.abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.abrir.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.abrir.setIcon(icon2)
        self.abrir.setObjectName(_fromUtf8("abrir"))
        self.opciones = QtGui.QPushButton(Menu)
        self.opciones.setGeometry(QtCore.QRect(10, 210, 231, 61))
        self.opciones.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opciones.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/opciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opciones.setIcon(icon3)
        self.opciones.setIconSize(QtCore.QSize(16, 16))
        self.opciones.setObjectName(_fromUtf8("opciones"))
        self.ayuda = QtGui.QPushButton(Menu)
        self.ayuda.setGeometry(QtCore.QRect(200, 10, 41, 41))
        self.ayuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ayuda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ayuda.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Ayuda.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ayuda.setIcon(icon4)
        self.ayuda.setIconSize(QtCore.QSize(32, 32))
        self.ayuda.setObjectName(_fromUtf8("ayuda"))
        self.pregunta = QtGui.QLabel(Menu)
        self.pregunta.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.pregunta.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"TeX Gyre Bonum\";"))
        self.pregunta.setObjectName(_fromUtf8("pregunta"))
        self.line = QtGui.QFrame(Menu)
        self.line.setGeometry(QtCore.QRect(10, 50, 231, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Menu)
        QtCore.QObject.connect(self.ayuda, QtCore.SIGNAL(_fromUtf8("clicked()")), Menu.ayuda)
        QtCore.QObject.connect(self.nuevo, QtCore.SIGNAL(_fromUtf8("clicked()")), Menu.nuevo)
        QtCore.QObject.connect(self.abrir, QtCore.SIGNAL(_fromUtf8("clicked()")), Menu.abrir)
        QtCore.QObject.connect(self.opciones, QtCore.SIGNAL(_fromUtf8("clicked()")), Menu.opciones)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "MarkYoun!", None))
        self.nuevo.setToolTip(_translate("Menu", "<html><head/><body><p><br/></p></body></html>", None))
        self.nuevo.setWhatsThis(_translate("Menu", "<html><head/><body><p>Crear nuevo archivo</p></body></html>", None))
        self.nuevo.setText(_translate("Menu", "Nuevo MarkDown", None))
        self.nuevo.setShortcut(_translate("Menu", "Return", "\"Ctrl+s\""))
        self.abrir.setToolTip(_translate("Menu", "<html><head/><body><p><br/></p></body></html>", None))
        self.abrir.setWhatsThis(_translate("Menu", "<html><head/><body><p align=\"center\">Precargar un archivo .md</p></body></html>", None))
        self.abrir.setText(_translate("Menu", "Abrir MarkDown", None))
        self.opciones.setToolTip(_translate("Menu", "<html><head/><body><p><br/></p></body></html>", None))
        self.opciones.setWhatsThis(_translate("Menu", "<html><head/><body><p align=\"center\">Cierre la Aplicación</p></body></html>", None))
        self.opciones.setText(_translate("Menu", "Opciones/Ajustes", None))
        self.ayuda.setWhatsThis(_translate("Menu", "<html><head/><body><p align=\"center\">Toque aquí si no sabe por donde empezar o quiere profundizar el programa</p></body></html>", None))
        self.pregunta.setText(_translate("Menu", "¿Qué desea hacer?", None))

