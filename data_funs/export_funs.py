import os
import pandas as pd

def export_car_to_csv(car_dict, kenteken):
    current_export_files_folders = os.listdir("export")

    if kenteken not in current_export_files_folders:
        print(f"Created folder {kenteken}")
        os.mkdir(f"export/{kenteken}")

    car_df = pd.DataFrame([car_dict])
    car_df.to_csv(f"export/{kenteken}/exported_car_{kenteken}.csv", sep=";", index=False)
    print(f"Exported car {kenteken} 🗄 ")


def export_cars_table_to_csv(df, brand):

    current_export_files_folders = os.listdir("export")

    if brand not in current_export_files_folders:
        print(f"Created folder {brand}")
        os.mkdir(f"export/{brand}")

    df.to_csv(f"export/{brand}/exported_{brand}_cars_list.csv", sep=";", index=False)
    print("Exported car 🎉")