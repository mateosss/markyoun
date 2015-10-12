echo "\n\n\n\n#-----Comenzando instalación de MarkYoun-----#\n\n\n\n"

echo "\n\n\n\n#-----Eliminando versiones anteriores de markyoun...-----#\n\n\n\n"
sudo rm -rf /usr/share/MarkYoun/
sudo rm /usr/applications/MarkYoun.desktop
sudo rm /bin/markyoun

echo "\n\n\n\n#-----Descargando componentes necesarios para la instalación-----#"
echo "unzip, python, python-qt4, pandoc, python-pip, librerías python markdown y pypandoc\n\n\n\n"
sudo apt-get install python -y
sudo apt-get install python-qt4 -y
sudo apt-get install pandoc -y
sudo apt-get install python-pip -y
sudo pip install markdown
sudo pip install pypandoc

echo "\n\n\n\n#-----Descargando MarkYoun desde dropbox...-----#\n\n\n\n"
wget https://www.dropbox.com/s/344jmx41hqulpdl/MarkYoun.zip
echo "\n\n\n\nDescomprimiendo...\n\n\n\n"
sudo mkdir /usr/
sudo mkdir /usr/share/
sudo mkdir /usr/share/MarkYoun/
sudo unzip -o MarkYoun.zip -d /usr/share/MarkYoun/

echo "\n\n\n\n#-----¿Desea descargar texlive y texlive-base?...-----#"
echo "Puede elegir no hacerlo, pero no podrá convertir sus archivos al formato pdf\n\n\n\n"
sudo apt-get install texlive texlive-base

echo "\n\n\n\n#-----Configurando compatibilidad con el sistema-----#"
cd /usr/share/MarkYoun/
sudo chmod +x MarkYoun
sudo cp /usr/share/MarkYoun/MarkYoun /bin/markyoun
sudo cp /usr/share/MarkYoun/MarkYoun.desktop /usr/share/applications/MarkYoun.desktop

#echo "\n\n\n\nUbicandolo en el escritorio, si no tiene el ejecutable estará en /home/USTED/MarkYoun/\n\n\n\n"
#cp $HOME/MarkYoun/MarkYoun $HOME/Escritorio/MarkYoun
#cp $HOME/MarkYoun/MarkYoun $HOME/Desktop/MarkYoun
#cp $HOME/MarkYoun/MarkYoun $HOME/MarkYoun

echo "\n\n\n\nEjecutando MarkYoun por primera vez...\n\n\n\n"
markyoun

echo "\n\n\n\nEliminando restos del instalador de MarkYoun de su equipo\n\n\n\n"
cd $HOME/
rm -f $HOME/MarkYoun.zip
rm -f $HOME/Downloads/distribute_setup.py
rm -f $HOME/instalador.sh
