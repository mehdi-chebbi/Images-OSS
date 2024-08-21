import requests
from datetime import datetime, timedelta, timezone

def human_readable_size(size_in_bytes):
    # Define size units
    units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    index = 0

    # Loop to find the appropriate unit
    while size_in_bytes >= 1024 and index < len(units) - 1:
        size_in_bytes /= 1024.0
        index += 1

    # Format size with unit
    return f"{size_in_bytes:.2f} {units[index]}"

def get_total_size(url):
    total_size = 0

    # Loop to fetch all pages
    while url:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Extract the ContentLength of each product and add to the total size
        for product in data.get('value', []):
            total_size += product.get('ContentLength', 0)

        # Get the next page link
        url = data.get('@odata.nextLink', None)

    return total_size

# Define the dates
today = datetime.now(timezone.utc).date()
start_date = today - timedelta(days=365)
start_date_str = start_date.strftime('%Y-%m-%dT00:00:00.000Z')
end_date_str = today.strftime('%Y-%m-%dT23:59:59.999Z')

# List of URLs and their descriptions
urls_and_descriptions = [
    (f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((ContentDate/Start%20ge%20{start_date_str}%20and%20ContentDate/Start%20le%20{end_date_str})%20and%20(Online%20eq%20true)%20and%20(OData.CSC.Intersects(Footprint=geography%27SRID=4326;POLYGON%20((8.155121%2036.344831,%209.076065%2036.344831,%209.076065%2037.080682612,%208.155121%2037.080682612,%208.155121%2036.344831))%27))%20and%20(((((Collection/Name%20eq%20%27SENTINEL-2%27)%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27S2MSI2A%27)))))))))&$expand=Attributes&$expand=Assets&$orderby=ContentDate/Start%20asc&$top=1000"
, 'L2A'),
    (f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((ContentDate/Start%20ge%20{start_date_str}%20and%20ContentDate/Start%20le%20{end_date_str})%20and%20(Online%20eq%20true)%20and%20(OData.CSC.Intersects(Footprint=geography%27SRID=4326;POLYGON%20((8.155121%2036.344831,%209.076065%2036.344831,%209.076065%2037.080682612,%208.155121%2037.080682612,%208.155121%2036.344831))%27))%20and%20(((((Collection/Name%20eq%20%27SENTINEL-1%27)%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27GRD%27))))%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27operationalMode%27%20and%20i0/Value%20eq%20%27IW%27)))))))))&$expand=Attributes&$expand=Assets&$orderby=ContentDate/Start%20asc&$top=1000"
, 'GRD-IW')
]

# Iterate over URLs and calculate sizes
for url, description in urls_and_descriptions:
    total_size = get_total_size(url)
    print(f"Total size of products for {description}: {human_readable_size(total_size)}")
