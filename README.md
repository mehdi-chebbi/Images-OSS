# OSS-FILTERED Project

This project contains scripts and tools for downloading Sentinel-2 L2A and Sentinel-1 GRD images using the Copernicus ODATA API. The scripts are designed to run in a cron job, requiring no human intervention.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- The `requests` library version 2.32.3.

## Installation

1. Clone the repository
    ```sh
    git clone https://github.com/mehdi-chebbi/oss-filtered.git
    ```

2. Install Python 3 if it's not already installed. You can download it from the [official Python website](https://www.python.org/downloads/).

3. Install the required Python package:
    ```sh
    pip install requests==2.32.3
    ```

## Configuration

Before using the scripts, create a `.env` file in the `OSS` folder with your Copernicus API credentials:

**Example `.env` file:**
USERNAME="Example_Username"
PASSWORD="Example_Password"

## Scripts Description

- `Download-GRD-L2A-DATA.sh` and `Download-GRD-L2A-DATA-Repating.sh`: Shell scripts to download GRD L2A data.
- `Get_GRD_IW_IDS.py` and `Get_GRD_IW_IDS_Repeating.py`: Python scripts to get GRD IW IDS.
- `Get_L2A_IDS.py` and `Get_L2A_IDS_Repeating.py`: Python scripts to get L2A IDS.
- `North_Africa_GRD_IW.sh` and `North_Africa_L2A.sh`: Shell scripts specific to North Africa data Donwloading.
- `Tunisia_GRD_IW.sh` and `Tunisia_L2A.sh`: Shell scripts specific to Tunisia data Donwloading.
- `Sentinel_data_size.py`: Python script to compute data size of Sentinel products.
- `README.md`: This file.
