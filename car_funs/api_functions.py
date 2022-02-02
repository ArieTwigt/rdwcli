import requests


def get_brands_list():
    url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?$query=SELECT DISTINCT(merk) WHERE voertuigsoort = 'Personenauto' ORDER BY merk ASC LIMIT 10000"
    resp = requests.get(url)
    if resp.status_code == 200:
        brands_dict = resp.json()
        brands_list = [list(brand.values())[0] for brand in brands_dict ]
    else:
        brands_list = ['Geen merken gevonden']
    return brands_list
    

def get_car_by_plate(plate):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}"
    resp = requests.get(endpoint)
    cars_list = resp.json()
    selected_car = cars_list[0]
    return selected_car


def get_car_by_brand(brand):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    resp = requests.get(endpoint)
    cars_list = resp.json()
    return cars_list