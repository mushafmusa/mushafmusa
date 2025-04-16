#!/bin/bash

echo "===== Radio FM Streamer ====="
echo "Author Musa"
echo "© 2025"
echo "1.Sgr Chanel  (98.7)"
echo "2.Zeno Chanel  (102.2)"
echo "3.Radionomy  (98.7)"
echo "4. Soma Fm (108.6)"
echo "5. Masukkan URL Stream Manual"
echo "============================="

read -p "Pilih stasiun radio / masukan Url [1-5)]: " choice

case $choice in
    1)
        mpv "http://stream.srg-ssr.ch/m/rsj/aacp_96"
        ;;
    2)
        mpv "http://stream.zeno.fm/f3wvbbqmdg8uv"
        ;;
    3)
        mpv "http://listen.radionomy.com/j-music-radio"
        ;;
    4)
        mpv "http://ice1.somafm.com/lush-128-mp3"
        ;;
    5)
        read -p "Masukkan URL stream radio: " url
        mpv "$url"
        ;;
    *)
        echo "Pilihan tidak valid"
        ;;
esac