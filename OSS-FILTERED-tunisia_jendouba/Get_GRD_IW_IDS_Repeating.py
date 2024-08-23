import requests
from datetime import datetime, timedelta, timezone
import os

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def load_last_fetched_id(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return file.readline().strip()
    return None

def save_last_fetched_id(last_id, file_name):
    with open(file_name, 'w') as file:
        file.write(last_id)

def save_product_ids(products, file):
    for product in products:
        product_id = product.get('Id')
        if product_id:
            file.write(f"Product ID: {product_id}\n")
            print(f"New Product ID: {product_id}")

today = datetime.now(timezone.utc).date()
start_date = today - timedelta(days=3)
start_date_str = start_date.strftime('%Y-%m-%dT00:00:00.000Z')
end_date_str = today.strftime('%Y-%m-%dT23:59:59.999Z')

url = f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((ContentDate/Start%20ge%20{start_date_str}%20and%20ContentDate/Start%20le%20{end_date_str})%20and%20(Online%20eq%20true)%20and%20(OData.CSC.Intersects(Footprint=geography%27SRID=4326;POLYGON%20((8.155121%2036.344831,%209.076065%2036.344831,%209.076065%2037.080682612,%208.155121%2037.080682612,%208.155121%2036.344831))%27))%20and%20(((((Collection/Name%20eq%20%27SENTINEL-1%27)%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27GRD%27))))%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27operationalMode%27%20and%20i0/Value%20eq%20%27IW%27)))))))))&$expand=Attributes&$expand=Assets&$orderby=ContentDate/Start%20asc&$top=1000"

last_fetched_id_file = 'last_fetched_id.txt'
last_fetched_id = load_last_fetched_id(last_fetched_id_file)

new_ids_found = False

with open('GRD-IW-IDS-Repeating', 'a') as file:
    while url:
        data = fetch_data(url)
        if data is None:
            break

        products = data.get('value', [])
        for product in products:
            product_id = product.get('Id')
            if product_id == last_fetched_id:
                url = None  # Stop the loop if the last fetched ID is found
                break
            if not last_fetched_id:
                new_ids_found = True
            save_product_ids([product], file)
            last_fetched_id = product_id  # Update last fetched ID

        url = data.get('@odata.nextLink')

if new_ids_found:
    save_last_fetched_id(last_fetched_id, last_fetched_id_file)
    print("New data saved.")
else:
    print("No new product IDs found today.")
