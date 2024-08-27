#!/bin/bash
cd /home/mehdi/oss/Images-OSS/OSS-FILTERED-north-africa
python3 Get_GRD_IW_IDS.py
python3 Get_L2A_IDS.py

mkdir -p IDS

mv GRD-IW-IDS IDS/
mv L2A-IDS IDS/

echo "Clearing GRD-IW-PRODUCTS folder contents..."
rm -rf "Products/GRD-IW-Products"/*

echo "Clearing L2A-PRODUCTS folder contents..."
rm -rf "Products/L2A-Products"/*




./North_Africa_GRD_IW.sh
./North_Africa_L2A.sh


# Unzip files in L2A and GRD-IW product directories
find Products/L2A-Products/ -type f -name "*.zip" -exec unzip -d Products/L2A-Products/ {} \;
find Products/GRD-IW-Products/ -type f -name "*.zip" -exec unzip -d Products/GRD-IW-Products/ {} \;

# Remove all zip files
find Products/L2A-Products/ -type f -name "*.zip" -delete
find Products/GRD-IW-Products/ -type f -name "*.zip" -delete
