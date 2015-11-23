#!/bin/bash
sudo apt-get install gtk-redshift
echo "Setting up Colortemp"
sudo mkdir /usr/share/Colortemp
sudo cp -avr ./* /usr/share/Colortemp
sudo touch /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo chmod 777 /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo cat bashinstruct.bash > /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo chmod +x /usr/share/Colortemp/dist/Colortemp/Colortemp.bash
sudo desktop-file-install ./.Desktop/Colortemp.desktop
sudo echo "alias colortemp='/usr/share/Colortemp/dist/Colortemp/Colortemp.bash'" >> ~/.bashrc
source ~/.bashrc
echo "Colortemp is installed and ready to use."
echo "Type \"colortemp\" on a terminal, or search your application menu."