#!/bin/bash

python3 Get_GRD_IW_IDS.py
python3 Get_L2A_IDS.py

mkdir -p IDS

mv GRD-IW-IDS IDS/
mv L2A-IDS IDS/

echo "Clearing GRD-IW-PRODUCTS folder contents..."
rm -rf "/mnt/c/Users/mehdi/Desktop/OSS-FILTERED/Products/GRD-IW-Products"/*

echo "Clearing L2A-PRODUCTS folder contents..."
rm -rf "/mnt/c/Users/mehdi/Desktop/OSS-FILTERED/Products/L2A-Products"/*




./Tunisia_GRD_IW.sh
./Tunisia_L2A.sh