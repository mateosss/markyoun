#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: latin1 -*-

#Crear nuevos iconos para funciones que no tienen y para las antiguas
#Actualizar utilidades MarkYoun
#instalador

#Arreglar el tema de los layouts del editor
#Acordarse de setear el cursor tipo beamer cuando termine todo en la seccion url y cambiar loadStarted() por urlChanged(const QUrl&)



#---><---#
#solucionar tema de imagenes del pdf internas file:///
#menejo de pestañas con archivos
#problema de rutas con puntos
#Buscar y reemplazar en el texto

import markdown
import pypandoc
import subprocess

from PyQt4 import QtCore, QtGui

import sys
import ConfigParser
import codecs

from Menu import Ui_Menu
from Editor import Ui_Editor
from Editor2 import Ui_Editor2
from Insertar import Ui_Insertar
from InsertarUtilidad import Ui_Utilidad
from SuperAyuda import Ui_Form
from Opciones import Ui_Opciones

reload(sys)
sys.setdefaultencoding("utf-8")

class Menu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Menu()
        self.ui.setupUi(self)

    def ayuda(self):
        myayuda.show()
            
    def nuevo(self):
        myeditor.show()
        self.close()
     
    def abrir(self):
        editor = myeditor
        editor.abrirArchivo()
        self.close()
        editor.show()
    
    def opciones(self):
        opciones = myopciones
        opciones.show()

class Opciones(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Opciones()
        self.ui.setupUi(self)

    def determinador(self,apretado):
        #determina que boton esta presionado y cual no
        #self.clasica.setChecked(True)        
        if apretado == "clasica":
            self.ui.rapida.setChecked(False)
        elif apretado == "rapida":
            self.ui.clasica.setChecked(False)
        elif apretado == "tradicional":
            self.ui.automatico.setChecked(False)
        elif apretado == "automatico":
            self.ui.tradicional.setChecked(False)
        else:
            self.mensaje("no hay nada que determinar")

    def clasica(self):
        self.determinador("clasica")
        self.director("interfaz","clasica")

    def rapida(self):
        self.determinador("rapida")
        self.director("interfaz","rapida")
    
    def tradicional(self):
        self.determinador("tradicional")
        self.director("guardado","tradicional")

    def automatico(self):
        self.determinador("automatico")
        self.director("guardado","automatico")

    def director(self,opcion,modo):
        #dirige al editor las variables de personalizacion
        editor = myeditor
        editor.setOpciones(opcion,modo)

class Editor(QtGui.QMainWindow):

    archivo = None

    def __init__(self, parent=None, archivo = "Nuevo Markdown.md"):
        QtGui.QWidget.__init__(self,parent)
        
        self.archivo = archivo
    
        config = ConfigParser.RawConfigParser()
        config.read("preferencias.cfg")

        cosa = config.get("preferencias","interfaz")
        guardado = config.get("preferencias","guardado")

        if cosa == "clasica":
            self.ui=Ui_Editor()
        elif cosa == "rapida":
            self.ui=Ui_Editor2()

        if guardado == "tradicional":
            self.guardado = "tradicional"
        elif guardado == "automatico":
            self.guardado = "automatico"

        self.ui.setupUi(self)
        limpiar = open(self.simplificarNombre(self.archivo)+".html","w")
        limpiar.close()
        if self.archivo != "Nuevo Markdown.md":
            fname = codecs.open(self.archivo,"r",encoding='utf-8')
            data = fname.read()
            self.ui.editando.clear()
            self.setTexto(data)
            self.nombreAMostrar(self.archivo)
            self.guardar()
            self.setPagina()        
        self.setPagina()


    def closeEvent(self, event):
        self.archivo = "Archivo restaurado.md"
        self.guardar()

    def setOpciones(self,opcion,modo):
        preferencias = "preferencias.cfg"
        #setea las opciones de las variables
        #de personalizacion y lo setea en un
        #archivo con config parser

        seccion = "preferencias"
        config = ConfigParser.RawConfigParser()
        config.read(preferencias)
        archivo = open(preferencias,"w")
        if config.has_section(seccion) == False:
            config.add_section(seccion)        

        if opcion == "guardado":
            self.guardado = modo
            #esto es para que luego vuelva a poner la url del archivo
            if modo == "automatico":
                if self.getTexto() != "":
                    self.guardar()
                    self.setPagina()
            config.set(seccion,"guardado",modo)
        elif opcion == "interfaz":
            self.interfaz = modo
            config.set(seccion,"interfaz",modo)
        else:
            self.mensaje("modo inexistente")
        config.write(archivo)
        archivo.close()

#Listeners...
#---------------------------------------------------------------#
    def seleccionLinea(self):
        #usada en la segunda interfaz markyown, deriva las 
        #opciones del QCombo box
        seleccionado = self.ui.seleccionLinea.currentText()
        if seleccionado == "1- Titulo":
            self.meterEnElMedio("formato","#")
        if seleccionado == "2- Titulo":
            self.meterEnElMedio("formato","##")
        if seleccionado == "3- Titulo":
            self.meterEnElMedio("formato","###")
        if seleccionado == "1- Cita":
            self.meterEnElMedio("formato",">")
        if seleccionado == "2- Cita":
            self.meterEnElMedio("formato",">>")
        if seleccionado == "3- Cita":
            self.meterEnElMedio("formato",">>>")
        if seleccionado == "Lista N":
            self.listaN()
        if seleccionado == "Lista":
            self.lista()
        if seleccionado == "Codigo":
            self.codigo()
            
        self.ui.seleccionLinea.setCurrentIndex(0)

    def seleccionFormato(self):
        #interfaz para seleccionar etiquetas html
        seleccionado = self.ui.seleccionFormato.currentText()
        if seleccionado == "Linea Divisora":
            self.linea()
        if seleccionado == "Negrita":
            self.negrita()
        if seleccionado == "Cursiva":
            self.cursiva()
        if seleccionado == "Subrayado":
            self.subrayado()
        if seleccionado == "Tachado":
            self.tachado()
        if seleccionado == "Texto Mayor":
            self.big()
        if seleccionado == "Texto Menor":
            self.small()
        if seleccionado == "Superindice":
            self.supind()
        if seleccionado == "Subindice":
            self.subind()
        if seleccionado == "Salto de Linea":
            self.saltoDeLinea()
        if seleccionado == "Parrafo a la Izquierda":
            self.parrIzq()
        if seleccionado == "Parrafo a la Derecha":
            self.parrDer()
        if seleccionado == "Parrafo Centrado":
            self.parrCen()

        self.ui.seleccionFormato.setCurrentIndex(0)
        
    def cambia(self):
        #esta funcion se ejecuta a cada momento y se fija si el 
        #guardado es de tipo tradicional o automatico
        if self.guardado == "automatico":
            self.guardar()
        elif self.guardado == "tradicional":
            self.transformarEnRam()
        else:
            self.mensaje("no se como llegate hasta aca")

    def guardar(self):
        #llama a save que guarda el archivo, luego a transformar
        #que lo transforma en html y guarda eso, y luego a
        #refrescar que reimprime en el visor html el archivo html
        if self.archivo == "Nuevo Markdown.md" and self.guardado != "automatico":
            self.guardarEn()
        self.save(self.archivo)
        self.transformar(str(self.archivo))
        self.refrescar()
        if self.ui==Ui_Editor2():
            urlAMostrar = self.ui.vistaHtml.url()
            self.ui.url.setText(urlAMostrar.toString())

    def restaurar(self):
        self.archivo = "Archivo restaurado.md"
        fname = codecs.open(self.archivo,"r",encoding='utf-8')
        data = fname.read()
        self.ui.editando.clear()
        self.setTexto(data)
        self.nombreAMostrar(self.archivo)

    def opciones(self):
        opciones = myopciones
        opciones.show()

    def abrirArchivo(self):
        # llama a la funcion abrir archivo..
        # luego de eso guarda ya que si fuese un archivo que 
        # no tiene
        # su .html respectivo daria error al setear la pagina en 
        # abirArchivoDialogo(), al guardar transformo y creo 
        #ese archivo y luego reseteo la pagina a la direccion
        #correcta que ahora si existe
        self.abrirArchivoDialogo()
        if self.archivo != "Nuevo Markdown.md" and self.archivo != "Archivo restaurado.md":

            self.guardar()
        self.setPagina()

    def guardarEn(self):
        self.guardarComo()
        if self.archivo!="Nuevo Markdown.md" and self.archivo != "Archivo restaurado.md":
            self.guardar()
            self.setPagina()

    def estaModificado(self):
        aux = self.ui.tabs.tabText(0)
        if aux[0]!="*":
            self.ui.tabs.setTabText(0,"*"+aux)
            return False
        else:
            return True
    
    def titulo(self):
        #tanto aqui como en cita,lista,etc. la funcion director
        #es una que dirige la escritura de caracteres simples de
        #la sintaxis de markdown. como #, o >>, etc.
        self.director("titulo")

    def back(self):
        self.ui.vistaHtml.back()

    def next(self):
        self.ui.vistaHtml.forward()

    def home(self):
        self.cambia()

    def buscarG(self):
        imagenes = self.ui.imagenes.isChecked()
        textoABuscar = self.ui.buscador.text()
        textAux = ""
        for i in textoABuscar:
            if i == " ":
                i = "+"
            textAux += i

        if imagenes:
            url = "https://www.google.com.ar/#q="+textAux+"&tbm=isch"
        else:
            url = "https://www.google.com.ar/#q="+textAux
        self.mensaje(textoABuscar+" ---------------> "+url)
        self.ui.vistaHtml.setUrl(QtCore.QUrl(url))

        urlAMostrar = self.ui.vistaHtml.url()
        if self.ui==Ui_Editor2():
            self.ui.url.setText(urlAMostrar.toString())

    def click(self):
        if self.ui==Ui_Editor2():
            urlAMostrar = self.ui.vistaHtml.url()
            self.ui.url.setText(urlAMostrar.toString())

    def cita(self):
        self.director("cita")

    def lista(self):
        self.director("lista")

    def listaN(self):
        self.director("listaN")

    def codigo(self):   
        self.director("codigo")   
    
    def linea(self):
        self.director("linea") 

    def negrita(self):
        self.director("negrita") 
  
    def cursiva(self):
        self.director("cursiva")

    def subrayado(self):
        self.director("subrayado")

    def tachado(self):
        self.director("tachado")

    def big(self):
        self.director("big")

    def small(self):
        self.director("small")

    def supind(self):
        self.director("supind")

    def subind(self):
        self.director("subind")

    def saltoDeLinea(self):
        self.director("saltoDeLinea")        

    def parrIzq(self):
        self.director("parrIzq")
    
    def parrDer(self):
        self.director("parrDer")

    def parrCen(self):
        self.director("parrCen")


    def insUtilidad(self):
        #abre la ventana myutilidad, clase Utilidad()
        myutilidad.show()

    def link(self): 
        #abre la vengana myinsertar, clase Insertar()
        myinsertar.show()
        myinsertar.ui.link.clear()
        myinsertar.ui.link.paste()


    def aHtml(self):
        self.guardar()

    def aPdf(self):
        self.pdf()

    def aOdt(self):
        self.odt()

    def aEpub(self):
        self.epub()


#Exportaciones
#---------------------------------------------------------------#
    def odt(self):
        self.convertir(self.archivo,"odt","odt")

    def docx(self):
        self.convertir(self.archivo,"docx","docx")

    def pdf(self):
        self.convertir(self.archivo, "pdf","pdf")

    def epub(self):
        self.convertir(self.archivo,"epub","epub")

    def epub3(self):
        self.convertir(self.archivo,"epub3","epub")

    def latex(self):
        self.convertir(self.archivo,"latex","tex")

    def plain(self):
        self.convertir(self.archivo,"plain","txt")

    def s5(self):
        self.convertir(self.archivo,"s5","s5")

    def man(self):
        self.convertir(self.archivo,"man","MAN") 

    def rst(self):
        self.convertir(self.archivo,"rst","rst")   

    def native(self):
        self.convertir(self.archivo,"native","native")

    def json(self):
        self.convertir(self.archivo,"json","json")

    def opendocument(self):
        self.convertir(self.archivo,"opendocument","opendocument")

    def beamer(self):
        self.convertir(self.archivo,"beamer","beamer")

    def context(self):
        self.convertir(self.archivo,"context","context")

    def texinfo(self):
        self.convertir(self.archivo,"texinfo","texinfo")

    def mediawiki(self):
        self.convertir(self.archivo,"mediawiki","mediawiki")

    def docbook(self):
        self.convertir(self.archivo,"docbook","docbook")

    def slidy(self):
        self.convertir(self.archivo,"slidy","slidy")

    def slideous(self):
        self.convertir(self.archivo,"slideous","slideous")

    def dzslides(self):
        self.convertir(self.archivo,"dzslides","dzslides")

    def rtf(self):
        self.convertir(self.archivo,"rtf","rtf")

    def org(self):
        self.convertir(self.archivo,"org","org")

    def asciidoc(self):
        self.convertir(self.archivo,"asciidoc","asciidoc")

#Funciones
#---------------------------------------------------------------#
    def director(self,modo):

        try:
        
            if modo == "titulo":
                if self.ui.opcTitulo.currentText() == "1- Titulo":
                    texto = "#"
        
                if self.ui.opcTitulo.currentText() == "2- Titulo":
                    texto = "##"
        
                if self.ui.opcTitulo.currentText() == "3- Titulo":
                    texto = "###"
        
                if self.ui.opcTitulo.currentText() == "4- Titulo":
                    texto = "####"
        
                if self.ui.opcTitulo.currentText() == "5- Titulo":
                    texto = "#####"
        
                if self.ui.opcTitulo.currentText() == "6- Titulo":
                    texto = "######"
                self.meterEnElMedio("formato",texto)
        except:
                self.meterEnElMedio("formato","#")
        
        if modo == "cita":
            try:
                if self.ui.opcCita.currentText() == "1 Cita":
                    texto = ">"
        
                if self.ui.opcCita.currentText() == "2 Cita":
                    texto = ">>"
            
                if self.ui.opcCita.currentText() == "3 Cita":
                    texto = ">>>"
            
                if self.ui.opcCita.currentText() == "4 Cita":
                    texto = ">>>>"
        
                if self.ui.opcCita.currentText() == "5 Cita":
                    texto = ">>>>>"
        
                if self.ui.opcCita.currentText() == "6 Cita":
                    texto = ">>>>>>"
        
                if self.ui.opcCita.currentText() == "7 Cita":
                    texto = ">>>>>>>"
        
                if self.ui.opcCita.currentText() == "8 Cita":
                    texto = ">>>>>>>>"
        
                if self.ui.opcCita.currentText() == "9 Cita":
                    texto = ">>>>>>>>>"
            
                if self.ui.opcCita.currentText() == "10 Cita":
                    texto = ">>>>>>>>>>"

                self.meterEnElMedio("formato",texto)
            except:
                self.ui.editando.append(">")
    
        if modo == "codigo":
            texto = "	"
            self.meterEnElMedio("formato",texto)

        if modo == "lista":
            texto = "- "
            self.meterEnElMedio("formato",texto)

        if modo == "listaN":
            texto = "1. "
            self.meterEnElMedio("formato",texto)
    
        if modo == "linea":
            texto = "-----------------------------------------\n"
            self.ui.editando.insertPlainText("\n"+texto) 
    
        if modo == "negrita":
            texto = u"****"
            self.meterEnElMedio(2,texto)
    
        if modo == "cursiva":
            texto = "**"
            self.meterEnElMedio(1,texto)

        if modo == "subrayado":
            texto = "<u></u>"
            self.meterEnElMedio(4,texto)

        if modo == "tachado":
            texto = "<del></del>"
            self.meterEnElMedio(6,texto)

        if modo == "big":
            texto = "<big></big>"
            self.meterEnElMedio(6,texto)

        if modo == "small":
            texto = "<small></small>"
            self.meterEnElMedio(8,texto)

        if modo == "supind":
            texto = "<sup></sup>"
            self.meterEnElMedio(6,texto)

        if modo == "subind":
            texto = "<sub></sub>"
            self.meterEnElMedio(6,texto)

        if modo == "saltoDeLinea":
            texto = "<br>"
            self.meterEnElMedio(0,texto)

        if modo == "parrIzq":
            texto = "<p align=left></p>"
            self.meterEnElMedio(4,texto)

        if modo == "parrDer":
            texto = "<p align=right></p>"
            self.meterEnElMedio(4,texto)

        if modo == "parrCen":
            texto = "<p align=center></p>"
            self.meterEnElMedio(4,texto)

#Funcionamiento Basico
#-----------------------------------------------------------#   

    def nuevo(self):
        #funcion que se ejecuta al hacer click en nuevo,
        # reseteo la ubicacion/nombre del archivo, limpio editor
        #seteo el texto de el TAB en "Nuevo", y seteo el visor
        #en la direccion de archivos correspondiente
        self.archivo = "Nuevo Markdown.md"
        self.ui.editando.clear()
        self.ui.tabs.setTabText(0,"Nuevo")
        self.setPagina()
    
    def guardarComo(self):
        #guarda el archivo en otro ya creado, especificamente 
        #sobre ese
        try:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar archivo como...','')
            if filename != "":
                self.nombreAMostrar(filename)
                self.archivo = self.simplificarNombre(filename)+".md"
                self.save(self.archivo)
        except:
            None

    
    def mensaje(self,mensaje):
        self.ui.statusbar.clearMessage()
        self.ui.statusbar.showMessage(mensaje)
        print(mensaje)

    def save(self,nombre):
        #guarda el archivo..
        archivo = codecs.open(nombre,"w",encoding='utf-8')
        self.mensaje("Se Guardo en "+nombre)
        archivo.write(self.getTexto())
        archivo.close()
        self.nombreAMostrar(self.archivo)

    def meterEnElMedio(self,modo,texto):
        #se utiliza en negrita y cursiva, para que al presionar
        #los botones respectivos el cursor de texto se 
        #acomode entre medio de los " * "
        cursor = self.ui.editando.textCursor()
        if modo != "formato":
            #guardo seleccion
            textoSeleccionado = cursor.selectedText()
            #inserto caracteres
            self.setTexto(texto)
            #muevo cursor la cantidad necesaria dada por modo
            columna = cursor.columnNumber()
            posicionActual = cursor.position()
            cursor.setPosition(posicionActual - modo, QtGui.QTextCursor.MoveAnchor)
            self.ui.editando.setTextCursor(cursor)
            #re pego el texto anteriormente seleccionado
            cursor.insertText(textoSeleccionado)
        else:
            posicionActual = cursor.position()
            columna = cursor.columnNumber()
            cursor.movePosition(QtGui.QTextCursor.StartOfLine)
            cursor.insertText(texto)
            cursor.movePosition(posicionActual)


    def transformar(self,nombre):
        #transforma el .md a .html y le agrega una linea extra
        #que permite que el archivo html sea compatible con utf-8
        nombreT = self.simplificarNombre(nombre)+".html"
        pepe = codecs.open(nombre,"r",encoding='utf-8')
        a = markdown.Markdown()
        a.convertFile( pepe, output=nombreT, encoding="utf-8")
        pepe.close()
        archivoHtml=codecs.open(nombreT,"r",encoding='utf-8')
        auxiliar = archivoHtml.read()
        archivoHtml.close()
        archivoHtml=codecs.open(nombreT,"w",encoding='utf-8')
        archivoHtml.write("\n"+"<meta charset=\"utf-8\" />"+"\n")
        archivoHtml.write(auxiliar)
        archivoHtml.close()
        self.mensaje(self.ui.statusbar.currentMessage()+" y se transformo en "+nombreT)

    def transformarEnRam(self):
        #esta funcion muestra el visor aunque el guardado este en tradicional

        editando = self.ui.editando
        textoMD = self.getTexto()
        a = markdown.Markdown()
        textoHTML = a.convert(str(textoMD))
        self.ui.vistaHtml.setHtml(textoHTML)
        self.acomodarVista()

        nombreT= self.simplificarNombre(self.archivo)+".html"        

        if self.ui==Ui_Editor2():
            urlAMostrar = QtCore.QUrl(nombreT)
            self.ui.url.setText(urlAMostrar.toString())

    def convertir(self,nombre,hacia,extension):
        #es la clase que usa la libreria pypandoc para 
        #para convertir los archivos determinando hacia
        #donde van
        #algunos como docx,odt,epub y epub3,
        #necesitan si o si del proceso pandoc,
        #ya que no se incluyen en la libreria
        nombre = self.simplificarNombre(nombre)+".html"
        nombreT = self.simplificarNombre(nombre)+"."+extension
        print(nombreT)
        self.guardar()
        if hacia != "docx" and hacia != "odt" and hacia != "epub" and hacia != "epub3" and hacia != "pdf":
            conversion = pypandoc.convert(nombre,hacia,format='md')
            archivo = open(nombreT,"w")
            archivo.write(conversion)
            archivo.close()
        else:
            if hacia == "docx" or hacia == "odt" or hacia == "epub" or hacia == "epub3" or hacia == "pdf":
                subprocess.call(['pandoc', '-o', nombreT, nombre])

        if nombreT != "Nuevo Markdown."+extension:
            self.mensaje("se ha convertido a "+hacia)
        else:
            self.mensaje("Ahora que has guardado procede a exportar nuevamente")
    def simplificarNombre(self,nombre):
        #genera un string de un archivo sin su extension para 
        #luego poder agregarsela en otros lugares
        nombreFinal = ""
        for i in str(nombre):
            if i != ".":
                nombreFinal += i
            else:
                break
        return nombreFinal
           
    def setPagina(self):
        #funcion utilizada en pocos casos, al hacer un Nuevo 
        #archivo, al abrir uno, y al guardar En otro archivo, 
        #setea la direccion web del visor por unica vez
        nombreT = self.simplificarNombre(self.archivo)+".html"

        if self.archivo == "Nuevo Markdown.md":
            self.ui.vistaHtml.setUrl(QtCore.QUrl("Nuevo Markdown.html"))

        else:
            self.ui.vistaHtml.setUrl(QtCore.QUrl(nombreT))

        urlAMostrar = self.ui.vistaHtml.url()
        if self.ui==Ui_Editor2():
            self.ui.url.setText(urlAMostrar.toString())

    def refrescar(self):
        #llama a acomodarVista() y relodea la pagina
        self.acomodarVista()
        self.ui.vistaHtml.reload()

    def acomodarVista(self):
        #acomoda la vista del visor html correspondientemente 
        #con la del QPlainTextEdit, esta en proceso.. ya que al 
        #momento de poner imagenes se desbalancea la proporcion 
        #pero igual sirve
        scrollEditorV = self.ui.editando.verticalScrollBar().sliderPosition()
        scrollEditorH = self.ui.editando.horizontalScrollBar().sliderPosition()
        self.ui.vistaHtml.page().mainFrame().setScrollPosition(QtCore.QPoint(scrollEditorH, scrollEditorV))


    def abrirArchivoDialogo(self):
        #abre un archivo del cual consigo su texto
        #su nombre completo(ruta), y luego a eso lo transformo
        #en un nombre simple para que aparezca en el TAB con ese 
        #"for"
        try:
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo','')
            fname = codecs.open(filename,"r",encoding='utf-8')
            data = fname.read()
            self.ui.editando.clear()
            self.setTexto(data)
            self.archivo = filename
            self.nombreAMostrar(filename)
        except: 
            None
    
    def nombreAMostrar(self,filename):
        #define un nombre pequeño sin la ruta
        #entera del archivo solo las ultimas 
        #palabras
        nombreAMostrar = ""
        for i in str(filename):
            if i != "/":
                nombreAMostrar += i
            else:
                nombreAMostrar = ""
        self.setWindowTitle('MarkYoun!: %s' %nombreAMostrar)
        self.ui.tabs.setTabText(0,nombreAMostrar)

    def getTexto(self):
        #funcion para obtener el texto del 
        #QPlainTextEdit(editando), de esta clase
        texto = self.ui.editando.toPlainText() 
        return texto
      
    def setTexto(self,texto):
        #funcion que inserta texto en el QPlainTextEdit
        self.ui.editando.insertPlainText(texto)

    
   
class Insertar(QtGui.QMainWindow):
    #clase para insertar videos, imagenes y links
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Insertar()
        self.ui.setupUi(self)
    
    def aceptar(self):
        #compruebo si los campos estan correctamente llenados 
        #o entrego error en un label, y luego llamo a la funcion
        #insertar de esta misma clase y la uso de la forma
        #conveniente segun quiero insertar video,imagen o link
        editor = myeditor
        nombre = self.ui.nombre.text()
        link = self.ui.link.text()
        if nombre != "" and link != "":
                texto=self.insertar()
                editor.setTexto(texto)
                self.close()
        elif self.ui.opcInsertar.currentText()=="Video de Youtube" or self.ui.opcInsertar.currentText() == "imagen" and link != "":
                texto = self.insertar()
                editor.setTexto(texto)
                self.close()
        else:
            self.ui.error.setText("Error, complete campos!!!!!!!!") 

    def insertar(self):
            #inserto texto en la otra clase(el editor)
            #dependiendo lo que este escrito en el 
            #combo box de esta clase
            nombre = self.ui.nombre.text()
            link = self.ui.link.text()
            descripcion = self.ui.descripcion.text()
            forma = self.ui.opcInsertar.currentText()
            if forma == "imagen":
                texto = "!["+nombre+"]("+link+" \""+descripcion+"\")"
            elif forma == "enlace":
                texto = "["+nombre+"]("+link+" \""+descripcion+"\")"
            elif forma == "Video de Youtube":
                link = str(link)
                link = link[len(link)-11 : len(link)]
                texto = "\n"+"<iframe width=\"640\" height=\"360\" src=\"http://www.youtube.com/embed/"+link+"?feature=player_detailpage\" frameborder=\"0\" allowfullscreen></iframe>"
            return texto


class Utilidad(QtGui.QMainWindow):
    #es la clase de la ventana de Utildades Markyoun, y 
    #es la que maneja la "Base de datos" del config parser y 
    #la muestra en la ventanita, puede modificar la base 
    #de datos o usar sus datos para escribirlos en el editor

    #archivo de configuraciones(config parser)
    archivo = "config.cfg"

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Utilidad()
        self.ui.setupUi(self)
        self.refrescarOpciones()

    def objetosLineEdit(self):
        #funcion hecha crear una lista en la cual poseo todos
        #los objetos(QLineEdit) de esta ventana, y me 
        #permite usar/modificar sus valores.
        escrito = [(self.ui.propiedad,self.ui.valor),
            (self.ui.propiedad_2,self.ui.valor_2),
            (self.ui.propiedad_3,self.ui.valor_3),
            (self.ui.propiedad_4,self.ui.valor_4),
            (self.ui.propiedad_5,self.ui.valor_5),
            (self.ui.propiedad_6,self.ui.valor_6),
            (self.ui.propiedad_7,self.ui.valor_7),
            (self.ui.propiedad_8,self.ui.valor_8),
            (self.ui.propiedad_9,self.ui.valor_9),
            (self.ui.propiedad_10,self.ui.valor_10),
            (self.ui.propiedad_11,self.ui.valor_11),
            (self.ui.propiedad_12,self.ui.valor_12)]
        return escrito  

    def refrescarOpciones(self):
        #refresca las opciones del comboBox, osea las secciones 
        #del config parser, los nombres de los diferentes codigos
        #html del COnfig parser
        nombre = self.archivo
        self.ui.opcUtilidad.clear()
        config = ConfigParser.RawConfigParser()
        config.read(nombre)
        res = config.sections()
        self.ui.opcUtilidad.addItems(res)
    
    def aceptar(self):
        #llama a asignar que escribe los datos de 
        #los QLineEdit en el editor
        self.asignar(self.archivo)

    def cambiar(self):
        #refresca lo escrito en los QLineEdit cuando 
        #el comboBox cambia
        self.definirElementos(self.archivo) 
 
    def eliminar(self):
        self.eliminarUtilidad(self.archivo)

    def guardar(self):
        #esta funcion llama a guardarUtilidad que guarda 
        #los datos de los QLineEdit en el archivo .cfg de 
        #config parser
        self.guardarUtilidad(self.archivo)

    def definirElementos(self,nombre):
        #declaro boxes, osea las cajas QLineEdit de la ventana
        boxes = self.objetosLineEdit()
        #borro todo lo que haya habido antes en esas cajas
        for i in range(len(boxes)):
            for j in range(2):
                boxes[i][j].setText("")
        
        #tomo la seccion a buscar del currentText del comboBox, 
        #y a partir de ahi comienzo a escribir sus "opciones" 
        #y "valores" de config parser en los cuadros
        config = ConfigParser.RawConfigParser()
        config.read(nombre)
        seccion = str(self.ui.opcUtilidad.currentText())
        try:
            items = config.items(seccion)
            self.ui.nombre.setText(seccion)
    
            for i in range(len(items)):
                propiedad = items[i][0]
                valor = items[i][1]
                boxes[i][0].setText(propiedad)
                boxes[i][1].setText(valor)
        except:
            None
    def asignar(self,nombre):
        #aqui escribo/asigno los VALORES que estaban escritos en
        #los QLineEdit, en el editor
        boxes = self.objetosLineEdit()
        editor = myeditor
        for i in range(len(boxes)):
            editor.ui.editando.insertPlainText(boxes[i][1].text())
        self.close()
        self.refrescarOpciones()
    
    def eliminarUtilidad(self,archivo):
        nombre = self.ui.nombre.text()
        config = ConfigParser.RawConfigParser()
        config.read(archivo)
        openfile = codecs.open(self.archivo,"w",encoding='utf-8')
        seccion = str(nombre)
        config.remove_section(seccion)
        config.remove_section("pepe")
        editor = myeditor
        editor.mensaje("se removio la utilidad: "+nombre)
        config.write(openfile)
        openfile.close()
        self.refrescarOpciones()

    def guardarUtilidad(self,archivo):
        #guarda la utilidad o cualquier cambio que se haya
        #hecho en la misma partiendo desde la casilla con 
        #el nombre, y recorriendo los valores que hay y no hay 
        #y modificandolos
        boxes = self.objetosLineEdit()
        nombre = self.ui.nombre.text()

        config = ConfigParser.RawConfigParser()
        config.read(archivo)
        openfile = codecs.open(self.archivo,"w",encoding='utf-8')
        seccion = str(nombre)
        #si tiene la seccion la limpia:
        if config.has_section(seccion) == True:
            for i in config.items(seccion):
               config.remove_option(seccion,i[0])
        #si no tiene la seccion
        elif config.has_section(seccion) == False:
            config.add_section(seccion)
        #rellena seccion
        for i in range(len(boxes)):        
            propiedad = str(boxes[i][0].text())
            valor = str(boxes[i][1].text())
            if propiedad != "":
                config.set(seccion,propiedad,valor)

        config.write(openfile)
        openfile.close()
        self.refrescarOpciones()

class Ayuda(QtGui.QMainWindow):
    #acerca de...
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    if len(sys.argv) == 1:
        myapp = Menu()
    if len(sys.argv) == 2:
        myapp = Editor(archivo = sys.argv[1])
        print(sys.argv[1])
    myopciones = Opciones()
    myapp.show()
    myeditor = Editor(None)
    myinsertar = Insertar()
    myutilidad = Utilidad()
    myayuda = Ayuda()

    sys.exit(app.exec_())
