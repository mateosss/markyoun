    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Opciones.ui'
#
# Created: Mon May 12 19:43:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ConfigParser
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

class Ui_Opciones(object):
    def setupUi(self, Opciones):

        config = ConfigParser.RawConfigParser()
        config.read("preferencias.cfg")
        guardado = config.get("preferencias","guardado")
        interfaz = config.get("preferencias","interfaz")

        Opciones.setObjectName(_fromUtf8("Opciones"))
        Opciones.resize(251, 284)
        Opciones.setMinimumSize(QtCore.QSize(251, 284))
        Opciones.setMaximumSize(QtCore.QSize(251, 284))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Opciones.setWindowIcon(icon)
        Opciones.setAutoFillBackground(False)

        self.clasica = QtGui.QPushButton(Opciones)
        self.clasica.setGeometry(QtCore.QRect(10, 100, 111, 61))
        self.clasica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clasica.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Editor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clasica.setIcon(icon1)
        self.clasica.setShortcut(_fromUtf8(""))
        self.clasica.setCheckable(True)
        if interfaz == "clasica":
            self.clasica.setChecked(True)
        self.clasica.setFlat(False)
        self.clasica.setObjectName(_fromUtf8("clasica"))
        self.automatico = QtGui.QPushButton(Opciones)
        self.automatico.setGeometry(QtCore.QRect(130, 210, 111, 61))
        self.automatico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.automatico.setFocusPolicy(QtCore.Qt.TabFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/Guardar.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.automatico.setIcon(icon2)
        self.automatico.setCheckable(True)
        if guardado == "automatico":
            self.automatico.setChecked(True)
        self.automatico.setObjectName(_fromUtf8("automatico"))
        self.pregunta = QtGui.QLabel(Opciones)
        self.pregunta.setGeometry(QtCore.QRect(20, 0, 221, 31))
        self.pregunta.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"TeX Gyre Bonum\";"))
        self.pregunta.setObjectName(_fromUtf8("pregunta"))
        self.line = QtGui.QFrame(Opciones)
        self.line.setGeometry(QtCore.QRect(10, 80, 231, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rapida = QtGui.QPushButton(Opciones)
        self.rapida.setGeometry(QtCore.QRect(130, 100, 111, 61))
        self.rapida.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rapida.setFocusPolicy(QtCore.Qt.TabFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/convertirOtros.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rapida.setIcon(icon3)
        self.rapida.setShortcut(_fromUtf8(""))
        self.rapida.setCheckable(True)
        if interfaz == "rapida":
            self.rapida.setChecked(True)
        self.rapida.setFlat(False)
        self.rapida.setObjectName(_fromUtf8("rapida"))
        self.line_2 = QtGui.QFrame(Opciones)
        self.line_2.setGeometry(QtCore.QRect(10, 190, 231, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pregunta_2 = QtGui.QLabel(Opciones)
        self.pregunta_2.setGeometry(QtCore.QRect(10, 50, 221, 31))
        self.pregunta_2.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"TeX Gyre Bonum\";"))
        self.pregunta_2.setObjectName(_fromUtf8("pregunta_2"))
        self.pregunta_3 = QtGui.QLabel(Opciones)
        self.pregunta_3.setGeometry(QtCore.QRect(10, 160, 221, 31))
        self.pregunta_3.setStyleSheet(_fromUtf8("font: 75 italic 14pt \"TeX Gyre Bonum\";"))
        self.pregunta_3.setObjectName(_fromUtf8("pregunta_3"))
        self.tradicional = QtGui.QPushButton(Opciones)
        self.tradicional.setGeometry(QtCore.QRect(10, 210, 111, 61))
        self.tradicional.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tradicional.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tradicional.setIcon(icon2)
        self.tradicional.setCheckable(True)
        if guardado == "tradicional":
            self.tradicional.setChecked(True)
        self.tradicional.setObjectName(_fromUtf8("tradicional"))
        self.label = QtGui.QLabel(Opciones)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 16))
        self.label.setStyleSheet(_fromUtf8("font: 75 7pt \"TeX Gyre Pagella\";"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Opciones)
        QtCore.QObject.connect(self.clasica, QtCore.SIGNAL(_fromUtf8("clicked()")), Opciones.clasica)
        QtCore.QObject.connect(self.rapida, QtCore.SIGNAL(_fromUtf8("clicked()")), Opciones.rapida)
        QtCore.QObject.connect(self.tradicional, QtCore.SIGNAL(_fromUtf8("clicked()")), Opciones.tradicional)
        QtCore.QObject.connect(self.automatico, QtCore.SIGNAL(_fromUtf8("clicked()")), Opciones.automatico)
        QtCore.QMetaObject.connectSlotsByName(Opciones)

    def retranslateUi(self, Opciones):
        Opciones.setWindowTitle(_translate("Opciones", "MarkYoun!", None))
        self.clasica.setToolTip(_translate("Opciones", "<html><head/><body><p><br/></p></body></html>", None))
        self.clasica.setWhatsThis(_translate("Opciones", "<html><head/><body><p>Crear nuevo archivo</p></body></html>", None))
        self.clasica.setText(_translate("Opciones", "Experto", None))
        self.automatico.setToolTip(_translate("Opciones", "<html><head/><body><p><br/></p></body></html>", None))
        self.automatico.setWhatsThis(_translate("Opciones", "<html><head/><body><p align=\"center\">Precargar un archivo .md</p></body></html>", None))
        self.automatico.setText(_translate("Opciones", "Automático", None))
        self.pregunta.setText(_translate("Opciones", "¿Cómo quiere que sea?", None))
        self.rapida.setToolTip(_translate("Opciones", "<html><head/><body><p><br/></p></body></html>", None))
        self.rapida.setWhatsThis(_translate("Opciones", "<html><head/><body><p>Crear nuevo archivo</p></body></html>", None))
        self.rapida.setText(_translate("Opciones", "Clásica", None))
        self.pregunta_2.setText(_translate("Opciones", "Diseño de interfaz:", None))
        self.pregunta_3.setText(_translate("Opciones", "Tipo de guardado:", None))
        self.tradicional.setToolTip(_translate("Opciones", "<html><head/><body><p><br/></p></body></html>", None))
        self.tradicional.setWhatsThis(_translate("Opciones", "<html><head/><body><p align=\"center\">Precargar un archivo .md</p></body></html>", None))
        self.tradicional.setText(_translate("Opciones", "Tradicional", None))
        self.label.setText(_translate("Opciones", "Tip: Reiniciar el programa luego de cambiar el diseño", None))

