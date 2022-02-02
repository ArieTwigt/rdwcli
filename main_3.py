from car_funs.api_functions import get_car_by_plate, get_car_by_brand
from data_funs.conversion_funs import conv_from_dict, conv_from_list
from data_funs.export_funs import export_car_to_csv, export_cars_table_to_csv

import argparse

# initiate an arg parser
parser = argparse.ArgumentParser()

# add arguments to the arg parser
parser.add_argument('--option', type=str, required=True)
parser.add_argument('--interactive', type=bool, required=True)
parser.add_argument('--plate', type=str, required=False, default=None)
parser.add_argument('--brand', type=str, required=False, default=None)

# create the arg parser
args = parser.parse_args()

if __name__ == '__main__':
    option = args.option

    interactive = args.interactive

    if option == 'plate':
        print(f"\n selected {option}\n")
        selected_plate = input("🚗 Insert your plate:\n") 
        car = get_car_by_plate(selected_plate)
        export_car_to_csv(car, selected_plate)
    elif option == 'brand':
        # get list of brands
        with open("cache/brands.txt", "r") as file:
            brand_list = file.readlines()
            brand_list_clean = [brand.replace("\n", "") for brand in brand_list]
            
        
        if interactive:

            selected_brand = args.brand

            if selected_brand is None:   
                print(f"\n selected {option}\n")
                print("\nChoose one of the following brands\n")
                brand_selection_str = "\n".join(brand_list_clean)
                print(brand_selection_str)
            
         
                selected_brand = input("Choose Brand:\n")
        cars_list = get_car_by_brand(selected_brand)
        cars_df = conv_from_list(cars_list)
        export_cars_table_to_csv(cars_df, selected_brand)
    else:
        print("Stopping script 👋")
        sys.exit()