#!/bin/bash

echo "Upgrading pkg ..."
apt update -y && apt upgrade -y >> /dev/null
echo "Pkg Upgraded successfully!"

echo "Installing pkg ..."
apt install -y python3 python3-pip figlet cowsay lolcat neofetch >> /dev/null
echo "Pkg Installed successfully!"

curl -o ~/bw.py -O https://raw.githubusercontent.com/yourtulloh/homeVPS/master/bw.py -s >> /dev/null
clear
echo "Input Header Name:"
read header_name
echo "Input Logo Name:"
read logo_name

echo -e "\n\ncowsay -f eyes $header_name | lolcat\nfiglet $logo_name | lolcat\ndate | lolcat\npython3 bw.py | lolcat" >> ~/.bashrc

echo "homeVPS Installed successfully. Now reconnect your VPS to take effect!"