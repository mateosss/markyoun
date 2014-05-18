# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Insertar.ui'
#
# Created: Mon May 12 19:42:45 2014
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

class Ui_Insertar(object):
    def setupUi(self, Insertar):
        Insertar.setObjectName(_fromUtf8("Insertar"))
        Insertar.resize(221, 317)
        Insertar.setMinimumSize(QtCore.QSize(221, 317))
        Insertar.setMaximumSize(QtCore.QSize(221, 317))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Insertar.setWindowIcon(icon)
        self.nombre = QtGui.QLineEdit(Insertar)
        self.nombre.setGeometry(QtCore.QRect(10, 50, 201, 29))
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.label = QtGui.QLabel(Insertar)
        self.label.setGeometry(QtCore.QRect(60, 30, 111, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Insertar)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 72, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.link = QtGui.QLineEdit(Insertar)
        self.link.setGeometry(QtCore.QRect(10, 100, 201, 29))
        self.link.setObjectName(_fromUtf8("link"))
        self.label_3 = QtGui.QLabel(Insertar)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 91, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.descripcion = QtGui.QLineEdit(Insertar)
        self.descripcion.setGeometry(QtCore.QRect(10, 150, 201, 29))
        self.descripcion.setObjectName(_fromUtf8("descripcion"))
        self.aceptar = QtGui.QPushButton(Insertar)
        self.aceptar.setGeometry(QtCore.QRect(30, 240, 171, 51))
        self.aceptar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Siguiente.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.aceptar.setIcon(icon1)
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.opcInsertar = QtGui.QComboBox(Insertar)
        self.opcInsertar.setGeometry(QtCore.QRect(40, 190, 151, 29))
        self.opcInsertar.setObjectName(_fromUtf8("opcInsertar"))
        self.opcInsertar.addItem(_fromUtf8(""))
        self.opcInsertar.addItem(_fromUtf8(""))
        self.opcInsertar.addItem(_fromUtf8(""))
        self.error = QtGui.QLabel(Insertar)
        self.error.setGeometry(QtCore.QRect(10, 300, 181, 19))
        self.error.setText(_fromUtf8(""))
        self.error.setObjectName(_fromUtf8("error"))

        self.retranslateUi(Insertar)
        QtCore.QObject.connect(self.aceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), Insertar.aceptar)
        QtCore.QMetaObject.connectSlotsByName(Insertar)

    def retranslateUi(self, Insertar):
        Insertar.setWindowTitle(_translate("Insertar", "Insertar...", None))
        self.label.setText(_translate("Insertar", "Figurara como", None))
        self.label_2.setText(_translate("Insertar", "   Link", None))
        self.label_3.setText(_translate("Insertar", "Descripción", None))
        self.aceptar.setText(_translate("Insertar", "ACEPTAR", None))
        self.opcInsertar.setItemText(0, _translate("Insertar", "imagen", None))
        self.opcInsertar.setItemText(1, _translate("Insertar", "enlace", None))
        self.opcInsertar.setItemText(2, _translate("Insertar", "Video de Youtube", None))

