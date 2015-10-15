#!/bin/bash
sudo apt-get install redshift
sudo apt-get install python-tk
sudo apt-get install python-pip
sudo pip install pyinstaller
pyinstaller ./src/Colortemp.py
sudo mkdir /usr/share/Colortemp
sudo cp -avr ./* /usr/share/Colortemp
sudo touch /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo chmod 777 /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo cat bashinstruct > /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo chmod +x /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo desktop-file-install ./.Desktop/Colortemp.desktop
sudo echo "alias colortemp='/usr/share/Colortemp/dist/Colortemp/Colortemp.bash'" >> ~/.bashrc
source ~/.bashrc
