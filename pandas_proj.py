
import pandas as pd
import json
from pandas import pivot_table, read_parquet

ecommerce_data_path_csv = "/Users/lionel/PyCharmMiscProject/src/data.csv"
ecommerce_data_df = pd.read_csv(ecommerce_data_path_csv, nrows=1000)
print(ecommerce_data_df)
print(ecommerce_data_df.dtypes)

ecommerce_data_df = ecommerce_data_df.convert_dtypes()

temp_dtype_df = ecommerce_data_df.astype({
    'Quantity': 'float64',
    'CustomerID': 'float64'
})
print(temp_dtype_df.dtypes)

read_sub_data = "/Users/lionel/PyCharmMiscProject/data/data_subset.json"
read_sub_data_df = pd.read_json(read_sub_data , encoding = 'unicode_escape')
print(read_sub_data_df.dtypes)


print(len(ecommerce_data_df) + len(read_sub_data_df))

ecommerce_data_df_append = pd.concat([ecommerce_data_df, read_sub_data_df])
print(ecommerce_data_df_append)

my_json = '{"Country" : ["United Kingdom", "France", "Australia", "Netherlands"], "Language":["English" , "French", "English" , "Dutch"]}'
data = json.loads(my_json)
df = pd.DataFrame(data)
print(df)

merge_df = pd.merge(ecommerce_data_df, df, on='Country')
print(merge_df)

ecommerce_data_df_append['InvoiceDate'] = pd.to_datetime(ecommerce_data_df_append['InvoiceDate'])
print(ecommerce_data_df_append.dtypes)

print(ecommerce_data_df_append.columns)

ecommerce_data_df_append =ecommerce_data_df_append.drop(["Country", "Quantity"], axis=1)
print(ecommerce_data_df_append.columns)

print(ecommerce_data_df_append.head(5))

#normalize

cols_to_normalize = ('Quantity','UnitPrice')

def absolute_maximum_scale(series):
    return series / series.abs().max()


for col in cols_to_normalize:
    ecommerce_data_df[col] = absolute_maximum_scale(ecommerce_data_df[col])


print(ecommerce_data_df.head(5))
print(ecommerce_data_df.Quantity)
print(ecommerce_data_df.UnitPrice)


#apply Lamda
ecommerce_data_df['UnitPrice'] = ecommerce_data_df['UnitPrice'].apply(lambda s: s * 100)
print(ecommerce_data_df.UnitPrice)

#Pivoting
print(ecommerce_data_df['Country'].unique())

ecommerce_data_df['unique_id'] = ecommerce_data_df['InvoiceNo'] + ecommerce_data_df['StockCode'] + ecommerce_data_df['CustomerID'].astype(str)
print(ecommerce_data_df.head(5))

ecommerce_pivot = (
    ecommerce_data_df
    .filter(items=["unique_id", "UnitPrice", "Country"])
    .pivot_table(
        index="unique_id",
        columns="Country",
        values="UnitPrice",
        aggfunc="mean"
    )
    .reset_index()
)

print(ecommerce_pivot)


#Parquet

ecommerce_pivot.to_parquet("/Users/lionel/PyCharmMiscProject/data/ecommerce_pivot.parquet.gzip",
                           compression='gzip')

read_parquett = pd.read_parquet("/Users/lionel/PyCharmMiscProject/data/ecommerce_pivot.parquet.gzip")
print(read_parquett)


#melting dataframes
print(ecommerce_data_df.head(25))
melted_df = ecommerce_data_df.melt(id_vars=["InvoiceNo"])
print(melted_df.head(25))


#normalize of json df

json_obj = {
    'InvoiceNo': '536370',
    'Quantity': 36,
    'InvoiceDate': '12/1/2010 8:45',
    'CustomerID': 2,
    'Country': 'France',
    'item': {
        'StockCode': 'John Kasich',
        'Description': 'MINI PAINT SET VINTAGE',
        'UnitPrice': 'UnitPrice'}
}
json_df_raw = pd.DataFrame.from_dict(json_obj)
print(json_df_raw.dtypes)

json_df_normalized = pd.json_normalize(json_obj)
print(json_df_normalized.dtypes)



