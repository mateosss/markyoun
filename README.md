![ ](https://dl.dropboxusercontent.com/u/105638235/logoMarkyoun.png "")

# MarkYoun!

- Para instalar necesitas una PC con una distro derivada de Ubuntu-Debian (Está probado unicamente en ubuntu, por favor reporta cualquier problema en otras distribuciones, y ayuda a hacer un mejor sistema de instalación, gracias)

    - To install you will need a Ubuntu-Debian based distro (It is proved only in ubuntu, please report issues in others distros, and help to make a better install system, thanks):


- Copia y pega en la terminal la siguiente linea:
    - Copy and paste in the terminal the next line:

    sudo wget https://raw.githubusercontent.com/mateosss/markyoun/master/instalador.sh && sudo chmod +x instalador.sh && sh instalador.sh -y

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
# Información de Desarrollo
## Problemas Actuales
-----------------------------------------
- Si la ruta tiene un punto que no es el de la extensión, MarkYoun!, guardará el archivo en rutas extrañas (en la misma con la primera carpeta que tenga un punto)
- Sigue en marcha lo del guardado tradicional
- Probando ideas para mejorar el rendimiento y fluidez de MarkYoun cuando se trabaja con archivos grandes

## Versiones Realizadas
-----------------------------------------
- v0.1 - inicial
- v0.2 - correcion de errores, desplazamiento paralelo del visor html con el editor de texto, capacidad de guardado en un archivo ya creado
- v0.2.1 - correccion de lectura de archivos en utf-8, y capacidad de guardar creando archivos nuevos
- v0.3 - inclusion de libreria pypandoc, exportacion a archivos de todo tipo. Mejora de UI interna.
- v0.4 - capacidad de cambio de interfaz estilo lyx, solucion del problema de utf8, creacion de un menu de opciones
- v0.4.1 - eleccion entre guardado automatico y normal
- v0.5 - mejoras en el sistema de guardado no automatico: pregunta antes de salir, guardar archivo de recuperacion,etc
- v0.9 - solucion de la mayor cantidad posible de bugs, mejora de ruidos visuales(whatsthis vacios)

## TODO

- [ ] tabulaciones de 4 espaciosh  
- [ ] comprobar en la vista html si la nueva posición a establecer en vertical
despues de modificar el texto es diferente a la que ya tiene para cambiarla 
(deberia ahorrar rendimiento)  
- [ ] Comprobar la vista html si esta en la posición lo más abajo posible, si es
así quedarse ahí siempre  
- [ ] se podria hacer un boton que haga que siempre se quede abajo y que se note
cuando este activado  
- [ ] nueva entrada de Menu -> Ver, para desactivar barra de estado, de 
herramientas, y la de "Archivo, Exportar" y la barra de busquedas  
- [ ] Desactivar generacion de html automatica  
- [ ] Capacidad de agregar temas(Fuente, color de fondo, de texto para seccion
MD y HTML (del ultimo tambien un CSS))  
- [ ] Sacar Pestaña de ayudame   
- [ ] Capacidad para tener varias pestañas  
- [ ] Drag and drop de archivos  
- [ ] Al borrar caracteres demora se laguea - fijarse cual es el problema  
- [ ] Accesos directos personalizables por archivo de configuracion  
- [ ] Fijarse si el html en ram puede ser modificado agregando cosas en lugar de
recargarlo entero  
- [ ] Revisar Instalador: que aparezca en menu accesorio, que aparezca para
abrir archivos de texto, que soporte "markyoun Archivo.md", revisar que 
soporte espacios y acentos y carpetas con puntos en los archivos a usar  
- [ ] Rehacer README  
- [ ] Agregar funcionalidad de buscar en el archivo CTRL-F  
- [ ] Hacer que la vista html se pueda desactivar o cambiar de tamaño (separar
en otra ventana?  
- [ ] Que m***** hacer con las utilidades MarkYoun? Mejorarlas? eliminarlas?
categorizarlas? dejar las mas utiles?   
- [ ] Tener más archivos de restauración (hasta unos 8) y que se puedan seleccionar
y que se guarden en la posición original agregandole .restaurado.md  
- [ ] Version para windows  
- [ ] Un posible cursor visible en el html?  
- [ ] Revisar por que no se guardo el archivo, RUTA: /home/mateo/Escritorio/Colegio/Higiene y Seguridad/Archivo1-1.png  
