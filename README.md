![](https://dl.dropboxusercontent.com/u/105638235/logoMarkyoun.png "")

#MarkYoun!

- Para instalar necesitas una PC con una distro derivada de Ubuntu-Debian (Está probado unicamente en ubuntu, por favor reporta cualquier problema en otras distribuciones, y ayuda a hacer un mejor sistema de instalación, gracias)

- To install you will need a Ubuntu-Debian based distro (It is proved only in ubuntu, please report issues in others distros, and help to make a better install system, thanks):

- Copia y pega en la terminal la siguiente linea:
- Copy and paste in the terminal the next line:

    sudo wget https://www.dropbox.com/s/4bt507ealvqtff9/instalador.sh && sudo chmod +x instalador.sh && sh instalador.sh -y

----------------------------------------

MarkYoun! Es actualmente un editor de markdown en tiempo real, que es liviano escrito en python hecho en pyqt4, y permite exportación a muchos formatos
además de html: org, man, epub, odt, etc. gracias a la librería **pypandoc** que puede encontrar aquí mismo en github.
Espero que lo pueda probar y ver sus capacidades, actualmente me gustaría tener colaboradores por lo menos con pequeños commits. 
Este programa es de carácter acádemico y para el uso diario, puedes hacer lo que quieras con el código
aunque agradecería que incluyas mi nombre. Mateo de Mayo o simplemente *"mateosss"*

----------------------------------------

MarkYoun!  Is actually a markdown editor in real time, it's light and it's written in python with pyqt4, it can export to a lot of different formats
in adittion of html: org, man, epub, odt, etc. thanks tp **pypandoc** library that you can find here in github.
I hope that you can prove it and see its capacities, I would like to have contributors to this proyect, at least for little commits.
The essence of this program is academic and for daily use,  you can do what you want with the code
but I hope that you include my name. Mateo de Mayo or simply *"mateosss"*


-----------------------------------------
-----------------------------------------
#Información de Desarrollo
##Problemas Actuales
-----------------------------------------
- Si la ruta tiene un punto que no es el de la extensión, MarkYoun!, guardará el archivo en rutas extrañas (en la misma con la primera carpeta que tenga un punto)
- Sigue en marcha lo del guardado tradicional
- Probando ideas para mejorar el rendimiento y fluidez de MarkYoun cuando se trabaja con archivos grandes

##Versiones Realizadas
-----------------------------------------
- v0.1 - inicial
- v0.2 - correcion de errores, desplazamiento paralelo del visor html con el editor de texto, capacidad de guardado en un archivo ya creado
- v0.2.1 - correccion de lectura de archivos en utf-8, y capacidad de guardar creando archivos nuevos
- v0.3 - inclusion de libreria pypandoc, exportacion a archivos de todo tipo. Mejora de UI interna.
- v0.4 - capacidad de cambio de interfaz estilo lyx, solucion del problema de utf8, creacion de un menu de opciones

##Futuras Versiones
-----------------------------------------
- v0.4.1 - eleccion entre guardado automatico y normal, y personalizacion de atajos de teclado
- v0.5 - mejoras en el sistema de guardado no automatico: pregunta antes de salir, guardar archivo de recuperacion,etc
- v0.9 - solucion de la mayor cantidad posible de bugs, mejora de ruidos visuales(whatsthis vacios), y utilidades de markyoun por tema
- v1.0 - Version estable y usable de forma optima, agregado de utilidades de todo tipo, (se espera tener más de 100), mejora de tutorial debería de haberse corregido el problema de la cantidad limitada a 512 carácteres utf-8 y al menos saber por que no se puede iniciar el texto con "f","e" o "u", solucionar el tema de la ayuda que aveces sale aveces no.

##Posibilidades a futuro
-----------------------------------------
- posibilidad de sincronizar con nubes(blogger,wordpress,)
- edicion paralela por internet(atravez de google docs por ejemplo), Dificil pero posible
- simulacion de edicion dentro del mismo visor web agregando un cursor de texto al visor
- mejoras en el visor web, botones de home, atras, busqueda de imagenes, de videos, de musica, y de insercion de links para probarlos
- separacion de utilidades del programa con las de usuario, visor web y editor capacidad de cambiar el espacio ocupado por cada uno
- capacidad de instalarlo en linux como un programa comun y corriente
- compilarlo para windows.
