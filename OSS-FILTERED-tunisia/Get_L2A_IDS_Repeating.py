import requests
from datetime import datetime, timedelta, timezone

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_product_ids(products, file):
    for product in products:
        product_id = product.get('Id')
        if product_id:
            file.write(f"Product ID: {product_id}\n")

today = datetime.now(timezone.utc).date()

start_date = today - timedelta(days=5)

start_date_str = start_date.strftime('%Y-%m-%dT00:00:00.000Z')
end_date_str = today.strftime('%Y-%m-%dT23:59:59.999Z')


url = f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((ContentDate/Start%20ge%20{start_date_str}%20and%20ContentDate/Start%20le%20{end_date_str})%20and%20(Online%20eq%20true)%20and%20(OData.CSC.Intersects(Footprint=geography%27SRID=4326;POLYGON%20((7.522749%2030.230347,%2011.611239%2030.230347,%2011.611239%2037.6320274,%207.522749%2037.6320274,%207.522749%2030.230347))%27))%20and%20(((((Collection/Name%20eq%20%27SENTINEL-2%27)%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27S2MSI2A%27)))))))))&$expand=Attributes&$expand=Assets&$orderby=ContentDate/Start%20asc&$top=1000"

with open('L2A-IDS', 'w') as file:
    while url:
        data = fetch_data(url)

        if data is None:
            break

        products = data.get('value', [])
        save_product_ids(products, file)

        url = data.get('@odata.nextLink')

print("Data saved to 'L2A-IDS' file.")
