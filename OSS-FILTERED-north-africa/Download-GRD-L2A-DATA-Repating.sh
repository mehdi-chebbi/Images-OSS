#!/bin/bash

python3 Get_GRD_IW_IDS_Repeating.py
python3 Get_L2A_IDS_Repeating.py

mkdir -p IDS

mv GRD-IW-IDS IDS/
mv L2A-IDS IDS/




./North_Africa_GRD_IW.sh
./North_Africa_L2A.sh