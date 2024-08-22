#!/bin/bash

python3 Get_GRD_IW_IDS_Repeating.py
python3 Get_L2A_IDS_Repeating.py

mkdir -p IDS

mv GRD-IW-IDS-Repeating IDS/
mv L2A-IDS-Repeating IDS/





./Tunisia_jendouba_GRD_IW_Repeating.sh
./Tunisia_jendouba_L2A_Repeating.sh