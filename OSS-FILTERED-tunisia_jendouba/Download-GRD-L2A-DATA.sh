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




./Tunisia_jendouba_GRD_IW.sh
./Tunisia_jendouba_L2A.sh

# Unzip files in L2A and GRD-IW product directories
find products/L2A-Products/ -type f -name "*.zip" -exec unzip -d products/L2A-Products/ {} \;
find products/GRD-IW-Products/ -type f -name "*.zip" -exec unzip -d products/GRD-IW-Products/ {} \;

# Remove all zip files
find products/L2A-Products/ -type f -name "*.zip" -delete
find products/GRD-IW-Products/ -type f -name "*.zip" -delete
