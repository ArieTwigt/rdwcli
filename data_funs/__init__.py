import os

current_files_directorie = os.listdir()

if "export" not in current_files_directorie:
    print("Created 'export' folder for your car exports")
    os.mkdir("export")