#!/bin/bash

ENV_FILE="../.env"

if [ -f "$ENV_FILE" ]; then
  export $(cat "$ENV_FILE" | xargs)
else
  echo ".env file not found!"
  exit 1
fi
CLIENT_ID="cdse-public"
TOKEN_URL="https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
OUTPUT_DIR="Products/L2A-Products"
IDS_FILE="IDS/L2A-IDS"

# Function to get the initial access token and refresh token
get_initial_tokens() {
  RESPONSE=$(curl --silent --location --request POST "$TOKEN_URL" \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode "grant_type=password" \
    --data-urlencode "username=$USERNAME" \
    --data-urlencode "password=$PASSWORD" \
    --data-urlencode "client_id=$CLIENT_ID")
  
  ACCESS_TOKEN=$(echo $RESPONSE | jq -r '.access_token')
  REFRESH_TOKEN=$(echo $RESPONSE | jq -r '.refresh_token')
}

# Function to refresh the access token
refresh_access_token() {
  RESPONSE=$(curl --silent --location --request POST "$TOKEN_URL" \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode "grant_type=refresh_token" \
    --data-urlencode "refresh_token=$REFRESH_TOKEN" \
    --data-urlencode "client_id=$CLIENT_ID")
  
  ACCESS_TOKEN=$(echo $RESPONSE | jq -r '.access_token')
  REFRESH_TOKEN=$(echo $RESPONSE | jq -r '.refresh_token')
}

# Function to download a product using the access token and product ID
download_product() {
  local product_id="$1"
  local output_file="$OUTPUT_DIR/product_$product_id.zip"
  
  curl -H "Authorization: Bearer $ACCESS_TOKEN" "https://catalogue.dataspace.copernicus.eu/odata/v1/Products($product_id)/\$value" --location-trusted --output "$output_file"
}

# Install jq if not already installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, installing..."
    sudo apt-get update
    sudo apt-get install -y jq
fi

# Get initial tokens
get_initial_tokens

# Create output directory if not exists
mkdir -p "$OUTPUT_DIR"
num_ids=$(wc -l < "$IDS_FILE")
echo "--------------------------------------------------------------------"
echo "Number of product concerning tunisia for the last 7 days:  $num_ids"
echo "--------------------------------------------------------------------"
# Read each line from the GRD_IDS file and download products
while IFS= read -r line; do
  if [[ "$line" =~ Product\ ID:\ (.*) ]]; then
    product_id="${BASH_REMATCH[1]}"
    download_product "$product_id"
    refresh_access_token
    sleep 5  # Adjust sleep time as needed
  fi
done < "$IDS_FILE"
