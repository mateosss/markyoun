# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperAyuda.ui'
#
# Created: Mon May 12 19:43:43 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(516, 422)
        Form.setMinimumSize(QtCore.QSize(516, 422))
        Form.setMaximumSize(QtCore.QSize(516, 422))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resource/utilidad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(498, 404))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Informacion", None))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Acerca de MarkYoun!</span></p><p align=\"center\"><br/></p><p align=\"center\">MarkYoun! es desarrollado por Mateo de Mayo</p><p align=\"center\">Utiliza las librerías PyQt4, pypandoc y markdown para su funcionamiento</p><p align=\"center\">Además de pandoc para la conversión de alguno de sus formatos</p><p align=\"center\"><br/></p><p align=\"center\">Este programa es completamente libre, puede hacer lo que quiera con él.</p><p align=\"center\">Puede encontrar el código fuente en <a href=\"http://www.github.com/mateosss/markyoun\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.github.com/mateosss/markyoun</span></a></p><p align=\"center\"><br/></p><p align=\"center\"><a href=\"http://www.github.com/mateosss/markyoun\"><span style=\" font-style:italic; text-decoration: underline; color:#000000;\">MarkYoun! Es un editor de archivos con extensión &quot;.md&quot; y apartir de los cuales</span></a></p><p align=\"center\"><a href=\"http://www.github.com/mateosss/markyoun\"><span style=\" font-style:italic; text-decoration: underline; color:#000000;\">puede generar diversos archivos con varios formatos gracias a pandoc</span></a></p><p align=\"center\"><br/></p></body></html>", None))

