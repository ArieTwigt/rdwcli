import json
from tqdm import tqdm

from car_funs.api_functions import get_car_by_brand
from data_funs.conversion_funs import conv_from_list
from data_funs.export_funs import export_cars_table_to_csv

with open("cars_config.json", "r") as file:
    cars_config = file.read()

cars_config_dict = json.loads(cars_config)
brands_list = cars_config_dict['brands']


for brand in brands_list:
    cars_list = get_car_by_brand(brand)
    cars_df = conv_from_list(cars_list)
    export_cars_table_to_csv(cars_df, brand)


