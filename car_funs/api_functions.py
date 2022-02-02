import requests


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