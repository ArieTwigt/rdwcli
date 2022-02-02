import os
from car_funs.api_functions import get_brands_list

current_files_directorie = os.listdir()

if "export" not in current_files_directorie:
    print("Created 'export' folder for your car exports")
    os.mkdir("export")


if "cache" not in current_files_directorie:
    print("📁 Cache folder not yet present, creating...")
    os.mkdir("cache")
    files_folders_cache = os.listdir("cache")
    
    if "cache/brands.txt" not in files_folders_cache:
        print("📄 Brands file not yet present, creating...")
        print("\n⏳\n")
        brands_list = get_brands_list() 
        print("\n✅ Brands imported\n")
        with open("cache/brands.txt", "w") as file:
            for brand in brands_list:
                file.write("%s\n" % brand)
