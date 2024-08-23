#!/bin/bash

python3 Get_GRD_IW_IDS_Repeating.py
python3 Get_L2A_IDS_Repeating.py

mkdir -p IDS

mv GRD-IW-IDS IDS/
mv L2A-IDS IDS/




./North_Africa_GRD_IW.sh
./North_Africa_L2A.sh


# Unzip files in L2A and GRD-IW product directories
find products/L2A-Products/ -type f -name "*.zip" -exec unzip -d products/L2A-Products/ {} \;
find products/GRD-IW-Products/ -type f -name "*.zip" -exec unzip -d products/GRD-IW-Products/ {} \;

# Remove all zip files
find products/L2A-Products/ -type f -name "*.zip" -delete
find products/GRD-IW-Products/ -type f -name "*.zip" -delete
