# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertarUtilidad.ui'
#
# Created: Mon May 12 19:42:58 2014
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

class Ui_Utilidad(object):
    def setupUi(self, Utilidad):
        Utilidad.setObjectName(_fromUtf8("Utilidad"))
        Utilidad.resize(373, 614)
        Utilidad.setMinimumSize(QtCore.QSize(373, 614))
        Utilidad.setMaximumSize(QtCore.QSize(373, 614))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/utilidadG.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Utilidad.setWindowIcon(icon)
        self.layoutWidget = QtGui.QWidget(Utilidad)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 451))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nombre = QtGui.QLineEdit(self.layoutWidget)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.verticalLayout.addWidget(self.nombre)
        self.splitter = QtGui.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.propiedad = QtGui.QLineEdit(self.splitter)
        self.propiedad.setObjectName(_fromUtf8("propiedad"))
        self.valor = QtGui.QLineEdit(self.splitter)
        self.valor.setObjectName(_fromUtf8("valor"))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_12 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.propiedad_2 = QtGui.QLineEdit(self.splitter_12)
        self.propiedad_2.setObjectName(_fromUtf8("propiedad_2"))
        self.valor_2 = QtGui.QLineEdit(self.splitter_12)
        self.valor_2.setObjectName(_fromUtf8("valor_2"))
        self.verticalLayout.addWidget(self.splitter_12)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.propiedad_3 = QtGui.QLineEdit(self.splitter_2)
        self.propiedad_3.setObjectName(_fromUtf8("propiedad_3"))
        self.valor_3 = QtGui.QLineEdit(self.splitter_2)
        self.valor_3.setObjectName(_fromUtf8("valor_3"))
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.propiedad_4 = QtGui.QLineEdit(self.splitter_3)
        self.propiedad_4.setText(_fromUtf8(""))
        self.propiedad_4.setObjectName(_fromUtf8("propiedad_4"))
        self.valor_4 = QtGui.QLineEdit(self.splitter_3)
        self.valor_4.setText(_fromUtf8(""))
        self.valor_4.setObjectName(_fromUtf8("valor_4"))
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.propiedad_5 = QtGui.QLineEdit(self.splitter_4)
        self.propiedad_5.setText(_fromUtf8(""))
        self.propiedad_5.setObjectName(_fromUtf8("propiedad_5"))
        self.valor_5 = QtGui.QLineEdit(self.splitter_4)
        self.valor_5.setText(_fromUtf8(""))
        self.valor_5.setObjectName(_fromUtf8("valor_5"))
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.propiedad_6 = QtGui.QLineEdit(self.splitter_5)
        self.propiedad_6.setText(_fromUtf8(""))
        self.propiedad_6.setObjectName(_fromUtf8("propiedad_6"))
        self.valor_6 = QtGui.QLineEdit(self.splitter_5)
        self.valor_6.setText(_fromUtf8(""))
        self.valor_6.setObjectName(_fromUtf8("valor_6"))
        self.verticalLayout.addWidget(self.splitter_5)
        self.splitter_6 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.propiedad_7 = QtGui.QLineEdit(self.splitter_6)
        self.propiedad_7.setText(_fromUtf8(""))
        self.propiedad_7.setObjectName(_fromUtf8("propiedad_7"))
        self.valor_7 = QtGui.QLineEdit(self.splitter_6)
        self.valor_7.setText(_fromUtf8(""))
        self.valor_7.setObjectName(_fromUtf8("valor_7"))
        self.verticalLayout.addWidget(self.splitter_6)
        self.splitter_7 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.propiedad_8 = QtGui.QLineEdit(self.splitter_7)
        self.propiedad_8.setText(_fromUtf8(""))
        self.propiedad_8.setObjectName(_fromUtf8("propiedad_8"))
        self.valor_8 = QtGui.QLineEdit(self.splitter_7)
        self.valor_8.setText(_fromUtf8(""))
        self.valor_8.setObjectName(_fromUtf8("valor_8"))
        self.verticalLayout.addWidget(self.splitter_7)
        self.splitter_8 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.propiedad_9 = QtGui.QLineEdit(self.splitter_8)
        self.propiedad_9.setText(_fromUtf8(""))
        self.propiedad_9.setObjectName(_fromUtf8("propiedad_9"))
        self.valor_9 = QtGui.QLineEdit(self.splitter_8)
        self.valor_9.setText(_fromUtf8(""))
        self.valor_9.setObjectName(_fromUtf8("valor_9"))
        self.verticalLayout.addWidget(self.splitter_8)
        self.splitter_9 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.propiedad_10 = QtGui.QLineEdit(self.splitter_9)
        self.propiedad_10.setText(_fromUtf8(""))
        self.propiedad_10.setObjectName(_fromUtf8("propiedad_10"))
        self.valor_10 = QtGui.QLineEdit(self.splitter_9)
        self.valor_10.setText(_fromUtf8(""))
        self.valor_10.setObjectName(_fromUtf8("valor_10"))
        self.verticalLayout.addWidget(self.splitter_9)
        self.splitter_10 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.propiedad_11 = QtGui.QLineEdit(self.splitter_10)
        self.propiedad_11.setText(_fromUtf8(""))
        self.propiedad_11.setObjectName(_fromUtf8("propiedad_11"))
        self.valor_11 = QtGui.QLineEdit(self.splitter_10)
        self.valor_11.setText(_fromUtf8(""))
        self.valor_11.setObjectName(_fromUtf8("valor_11"))
        self.verticalLayout.addWidget(self.splitter_10)
        self.splitter_11 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.propiedad_12 = QtGui.QLineEdit(self.splitter_11)
        self.propiedad_12.setText(_fromUtf8(""))
        self.propiedad_12.setObjectName(_fromUtf8("propiedad_12"))
        self.valor_12 = QtGui.QLineEdit(self.splitter_11)
        self.valor_12.setText(_fromUtf8(""))
        self.valor_12.setObjectName(_fromUtf8("valor_12"))
        self.verticalLayout.addWidget(self.splitter_11)
        self.label = QtGui.QLabel(Utilidad)
        self.label.setGeometry(QtCore.QRect(10, 470, 128, 128))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Resource/utilidadG.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.usar = QtGui.QPushButton(Utilidad)
        self.usar.setGeometry(QtCore.QRect(170, 510, 191, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usar.sizePolicy().hasHeightForWidth())
        self.usar.setSizePolicy(sizePolicy)
        self.usar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usar.setIcon(icon)
        self.usar.setIconSize(QtCore.QSize(32, 32))
        self.usar.setFlat(False)
        self.usar.setObjectName(_fromUtf8("usar"))
        self.guardarUtilidad = QtGui.QPushButton(Utilidad)
        self.guardarUtilidad.setGeometry(QtCore.QRect(170, 560, 91, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guardarUtilidad.sizePolicy().hasHeightForWidth())
        self.guardarUtilidad.setSizePolicy(sizePolicy)
        self.guardarUtilidad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guardarUtilidad.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Editor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guardarUtilidad.setIcon(icon1)
        self.guardarUtilidad.setIconSize(QtCore.QSize(32, 32))
        self.guardarUtilidad.setFlat(False)
        self.guardarUtilidad.setObjectName(_fromUtf8("guardarUtilidad"))
        self.opcUtilidad = QtGui.QComboBox(Utilidad)
        self.opcUtilidad.setGeometry(QtCore.QRect(170, 470, 191, 27))
        self.opcUtilidad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opcUtilidad.setObjectName(_fromUtf8("opcUtilidad"))
        self.eliminar = QtGui.QPushButton(Utilidad)
        self.eliminar.setGeometry(QtCore.QRect(270, 560, 91, 41))
        self.eliminar.setObjectName(_fromUtf8("eliminar"))

        self.retranslateUi(Utilidad)
        QtCore.QObject.connect(self.usar, QtCore.SIGNAL(_fromUtf8("clicked()")), Utilidad.aceptar)
        QtCore.QObject.connect(self.guardarUtilidad, QtCore.SIGNAL(_fromUtf8("clicked()")), Utilidad.guardar)
        QtCore.QObject.connect(self.opcUtilidad, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Utilidad.cambiar)
        QtCore.QObject.connect(self.eliminar, QtCore.SIGNAL(_fromUtf8("clicked()")), Utilidad.eliminar)
        QtCore.QMetaObject.connectSlotsByName(Utilidad)

    def retranslateUi(self, Utilidad):
        Utilidad.setWindowTitle(_translate("Utilidad", "Insertor de utilidad", None))
        self.nombre.setText(_translate("Utilidad", "nombre de utilidad: completar si se guardara", None))
        self.propiedad.setText(_translate("Utilidad", "Propiedad", None))
        self.valor.setText(_translate("Utilidad", "Valor", None))
        self.propiedad_2.setText(_translate("Utilidad", "Propiedad", None))
        self.valor_2.setText(_translate("Utilidad", "Valor", None))
        self.propiedad_3.setText(_translate("Utilidad", "Propiedad", None))
        self.valor_3.setText(_translate("Utilidad", "Valor", None))
        self.usar.setText(_translate("Utilidad", "Usar", None))
        self.guardarUtilidad.setText(_translate("Utilidad", "Guardar", None))
        self.eliminar.setText(_translate("Utilidad", "Eliminar", None))

