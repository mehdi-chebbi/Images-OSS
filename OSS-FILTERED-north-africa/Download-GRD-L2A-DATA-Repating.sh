#!/bin/bash

# Navigate to the working directory
cd /home/mehdi/os/Images-OSS/OSS-FILTERED-north-africa

# Run Python scripts and capture their outputs
grd_output=$(python3 Get_GRD_IW_IDS_Repeating.py)
l2a_output=$(python3 Get_L2A_IDS_Repeating.py)

# Check for "No new product IDs found today." in the outputs
if echo "$grd_output" | grep -q "No new product IDs found today." && \
   echo "$l2a_output" | grep -q "No new product IDs found today."; then
    echo "No new product IDs found today. Stopping the script."
    exit 0
fi

# Create IDS directory and move files
mkdir -p IDS
mv GRD-IW-IDS IDS/
mv L2A-IDS IDS/

# Run additional shell scripts
./North_Africa_GRD_IW.sh
./North_Africa_L2A.sh

# Unzip files in L2A and GRD-IW product directories
find products/L2A-Products/ -type f -name "*.zip" -exec unzip -d products/L2A-Products/ {} \;
find products/GRD-IW-Products/ -type f -name "*.zip" -exec unzip -d products/GRD-IW-Products/ {} \;

# Remove all zip files
find products/L2A-Products/ -type f -name "*.zip" -delete
find products/GRD-IW-Products/ -type f -name "*.zip" -delete
