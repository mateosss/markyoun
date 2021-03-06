echo "\n\n\n\n#-----Comenzando instalación de MarkYoun-----#\n\n\n\n"

echo "\n\n\n\n#-----¿Desea descargar texlive y texlive-base?...-----#"
echo "Puede elegir no hacerlo, pero no podrá convertir sus archivos al formato pdf"
echo "No se le volverá a preguntar nada durante la instalación, puede ir a tomar un café.\n\n\n\n"
sudo apt-get install texlive texlive-base

echo "\n\n\n\n#-----Eliminando versiones anteriores de markyoun...-----#\n\n\n\n"
sudo rm -rf /home/$LOGNAME/MarkYoun/
sudo rm /usr/applications/MarkYoun.desktop
sudo rm /bin/markyoun

echo "\n\n\n\n#-----Descargando componentes necesarios para la instalación-----#"
echo "unzip, python, python-qt4, pandoc, python-pip, librerías python markdown y pypandoc\n\n\n\n"
sudo apt-get install git python python-qt4 pandoc python-pip -y
sudo pip install markdown
sudo pip install pypandoc

echo "\n\n\n\n#-----Descargando MarkYoun desde GitHub...-----#\n\n\n\n"
#wget https://www.dropbox.com/s/344jmx41hqulpdl/MarkYoun.zip
cd
git clone https://github.com/mateosss/markyoun MarkYoun

echo "\n\n\n\n#-----Configurando compatibilidad con el sistema-----#"
cd /home/$LOGNAME/MarkYoun/
sudo chmod +x MarkYoun
sudo cp /home/$LOGNAME/MarkYoun/MarkYoun /bin/markyoun
sudo cp /home/$LOGNAME/MarkYoun/MarkYoun.desktop /usr/share/applications/MarkYoun.desktop
sudo mkdir /usr/
sudo mkdir /usr/share
sudo mkdir /usr/share/MarkYoun
sudo mkdir /usr/share/MarkYoun/icons/
sudo cp /home/$LOGNAME/MarkYoun/Nuevos\ Iconos/Creando\ Iconos/svg/icono.png /usr/share/MarkYoun/icons/icono.png

sudo cp /home/$LOGNAME/MarkYoun/
#echo "\n\n\n\nUbicandolo en el escritorio, si no tiene el ejecutable estará en /home/USTED/MarkYoun/\n\n\n\n"
#cp $HOME/MarkYoun/MarkYoun $HOME/Escritorio/MarkYoun
#cp $HOME/MarkYoun/MarkYoun $HOME/Desktop/MarkYoun
#cp $HOME/MarkYoun/MarkYoun $HOME/MarkYoun

echo "\n\n\n\nEliminando restos del instalador de MarkYoun de su equipo\n\n\n\n"
cd $HOME/
rm -f $HOME/MarkYoun.zip
rm -f $HOME/Downloads/distribute_setup.py
rm -f $HOME/instalador.sh

echo "\n\n\n\nEjecutando MarkYoun por primera vez...\n\n\n\n"
markyoun