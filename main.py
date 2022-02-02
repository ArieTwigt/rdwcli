from car_funs.api_functions import get_car_by_plate, get_car_by_brand
from data_funs.conversion_funs import conv_from_dict, conv_from_list
from data_funs.export_funs import export_car_to_csv, export_cars_table_to_csv

import sys

if __name__ == '__main__':

    option = input("Select car by brand or by plate ('brand'/'plate')\n") or 'brand'

    
    if option == 'plate':
        print(f"\n selected {option}\n")
        selected_plate = input("🚗 Insert your plate:\n")
        car = get_car_by_plate(selected_plate)
        export_car_to_csv(car, selected_plate)
    elif option == 'brand':
        print(f"\n selected {option}\n")
        selected_brand = input("Choose Brand:\n") or "TESLA"
        cars_list = get_car_by_brand(selected_brand)
        cars_df = conv_from_list(cars_list)
        export_cars_table_to_csv(cars_df, selected_brand)
    else:
        print("Stopping script 👋")
        sys.exit()



    
    

    
    
