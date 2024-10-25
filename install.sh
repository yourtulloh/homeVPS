#!/bin/bash

# Bersihkan terminal
clear

# Update dan upgrade paket sistem
echo "Menjalankan apt update & upgrade... Mohon tunggu!"
sudo apt update && sudo apt upgrade -y

# Instal paket yang diperlukan
echo "Menginstal paket yang dibutuhkan... Mohon tunggu!"
sudo apt install -y python3 python3-pip docker-compose figlet cowsay lolcat neofetch git certbot nginx python3-certbot-nginx timedatectl

# Unduh skrip Python
curl -o ~/bw.py -O https://raw.githubusercontent.com/yourtulloh/homeVPS/master/bw.py -s

# Set zona waktu
sudo timedatectl set-timezone Asia/Jakarta
clear
# Pesan konfirmasi
echo "Paket telah berhasil diinstal!" | lolcat

# Minta input nama header dan logo dari pengguna
echo "Masukkan Nama Header:" | lolcat
read header_name
echo "Masukkan Nama Logo:" | lolcat
read logo_name

# Tambahkan perintah ke .bashrc
echo -e "\ncowsay -f eyes $header_name | lolcat\nfiglet $logo_name | lolcat\ndate | lolcat\npython3 ~/bw.py | lolcat" >> ~/.bashrc

# Tampilkan pesan sukses
figlet HomeVPS | lolcat
echo "Instalasi berhasil. Silakan sambungkan kembali VPS Anda agar perubahan berlaku!" | lolcat

# Bersihkan terminal dan jalankan skrip Python
clear
python3 ~/bw.py