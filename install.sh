#!/bin/bash
echo "Installing & Upgrading pkg ..."
apt update -y && apt upgrade -y > /dev/null
echo "Pkg Upgraded successfully!"
apt install -y curl git python3 python3-pip figlet cowsay lolcat neofetch > /dev/null
echo "Pkg Installed successfully!"