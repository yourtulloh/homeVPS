#!/bin/bash
clear
echo "Installing pkg: python3 python3-pip figlet cowsay lolcat neofetch ... Please wait!"
apt install -y python3 python3-pip figlet cowsay lolcat neofetch > /dev/null
curl -o ~/bw.py -O https://raw.githubusercontent.com/yourtulloh/homeVPS/master/bw.py -s > /dev/null
clear
echo "Pkg Installed successfully!" | lolcat
echo "Input Header Name:" | lolcat
read header_name
echo "Input Logo Name:" | lolcat
read logo_name

echo -e "\n\ncowsay -f eyes $header_name | lolcat\nfiglet $logo_name | lolcat\ndate | lolcat\npython3 bw.py | lolcat" >> ~/.bashrc
figlet HomeVPS | lolcat
echo "Installed successfully. Now reconnect your VPS to take effect!" | lolcat
python3 bw.py