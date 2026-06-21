import pandas as pd
import numpy as np

ecommerce_data_path_csv = "/Users/lionel/PyCharmMiscProject/src/data.csv"
ecommerce_data_df = pd.read_csv(ecommerce_data_path_csv, nrows=1000)
print(ecommerce_data_df)
print(ecommerce_data_df.dtypes)

quantity_array = np.array(ecommerce_data_df["Quantity"].to_numpy())
print(np.mean(quantity_array))
print(quantity_array)

print(np.max(quantity_array))
print(np.min(quantity_array))

#randomint
ecommerce_data_df['user_id'] = np.random.randint(1,10,ecommerce_data_df.shape[0])
print(ecommerce_data_df)
print(ecommerce_data_df.dtypes)