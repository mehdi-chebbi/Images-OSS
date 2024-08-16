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


url = f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((ContentDate/Start%20ge%20{start_date_str}%20and%20ContentDate/Start%20le%20{end_date_str})%20and%20(Online%20eq%20true)%20and%20(OData.CSC.Intersects(Footprint=geography%27SRID=4326;POLYGON%20((-16.535376%2015.648902,%20-16.082942%2016.518848,%20-14.318447%2016.605631,%20-11.965787%2014.556266,%20-9.296423%2015.474461,%20-5.224511%2015.474461,%20-4.907807%2016.345165,%20-5.405485%2016.735732,%20-6.627059%2024.811516,%20-4.636346%2024.893671,%203.326503%2018.67626,%206.267328%2019.44643,%2012.013247%2023.489719,%2014.230177%2022.405875,%2016.130402%2023.323541,%2024.274225%2019.275592,%2024.228982%2019.915306,%2025.179094%2020.127975,%2025.314825%2021.860738,%2037.168611%2022.028696,%2035.901794%2023.073884,%2035.947038%2024.358694,%2034.318273%2026.767894,%2034.137299%2027.372546,%2035.042169%2029.403503,%2034.27303%2031.317372,%2031.241718%2031.89569,%2026.717372%2031.626255,%2024.590929%2032.317497,%2021.966809%2033.155232,%2019.387931%2033.04146,%2019.478418%2031.239992,%2018.618792%2030.968664,%2016.130402%2031.780314,%2014.727855%2032.96553,%2011.832273%2033.797149,%2011.244108%2034.322201,%2011.78703%2035.214682,%2011.379839%2036.134029,%2011.832273%2036.970428,%2011.696543%2037.582797,%209.841561%2037.690345,%207.669875%2037.475094,%203.68845%2037.401314,%201.426277%2036.986607,%20-1.582413%2035.83906,%20-2.374173%2035.508086,%20-3.708855%2035.636961,%20-5.134024%2036.040646,%20-6.106759%2035.83906,%20-7.237845%2034.413652,%20-7.961741%2033.851582,%20-10.382266%2031.46991,%20-10.065562%2030.167567,%20-11.807435%2028.788293,%20-13.662417%2027.59132,%20-15.087586%2025.771214,%20-16.241294%2023.591291,%20-17.259272%2021.311293,%20-16.852081%2019.955625,%20-16.648485%2018.716885,%20-16.399646%2017.274584,%20-16.535376%2015.648902))%27))%20and%20(((((Collection/Name%20eq%20%27SENTINEL-2%27)%20and%20(((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27S2MSI2A%27)))))))))&$expand=Attributes&$expand=Assets&$orderby=ContentDate/Start%20asc&$top=1000"

with open('L2A-IDS', 'w') as file:
    while url:
        data = fetch_data(url)

        if data is None:
            break

        products = data.get('value', [])
        save_product_ids(products, file)

        url = data.get('@odata.nextLink')

print("Data saved to 'L2A-IDS' file.")
