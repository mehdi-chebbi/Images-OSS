# Run Python scripts
python3 Get_GRD_IW_IDS_Repeating.py
python3 Get_L2A_IDS_Repeating.py

# Create IDS directory and move files
mkdir -p IDS
mv GRD-IW-IDS-Repeating IDS/
mv L2A-IDS-Repeating IDS/

# Run additional shell scripts
./Tunisia_jendouba_GRD_IW_Repeating.sh
./Tunisia_jendouba_L2A_Repeating.sh

# Unzip files in L2A and GRD-IW product directories
find products/L2A-Products/ -type f -name "*.zip" -exec unzip -d products/L2A-Products/ {} \;
find products/GRD-IW-Products/ -type f -name "*.zip" -exec unzip -d products/GRD-IW-Products/ {} \;

# Remove all zip files
find products/L2A-Products/ -type f -name "*.zip" -delete
find products/GRD-IW-Products/ -type f -name "*.zip" -delete
