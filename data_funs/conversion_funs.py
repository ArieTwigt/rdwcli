import pandas as pd


def conv_from_dict(input_dict):
    df_car = pd.DataFrame([input_dict])
    return df_car


def conv_from_list(input_list):
    df_cars = pd.DataFrame(input_list)
    return df_cars
    