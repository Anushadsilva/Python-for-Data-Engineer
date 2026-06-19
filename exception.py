import pandas as pd
e_commerce_fake_path_csv = "./data/fake_path.csv"

try:
    e_commerce_fake_path_csv_df = pd.read_csv(e_commerce_fake_path_csv, encoding ='unicode_escape'
                                    , nrows = 1000)
except:
    print("File not exist")

try:
    e_commerce_fake_path_csv_df = pd.read_csv(e_commerce_fake_path_csv, encoding ='unicode_escape'
                                    , nrows = 1000)
except FileNotFoundError as error:
    print(f'{error}, provide correct path')

