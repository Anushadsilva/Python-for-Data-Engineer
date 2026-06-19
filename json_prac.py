import json


with open("/Users/lionel/PyCharmMiscProject/jsn.json") as json_file:
    data = json.load(json_file)
    print(data)


json_formatted_string = json.dumps(data)
print(json_formatted_string)

trans_list_of_dicts = json.loads(json_formatted_string)
print(trans_list_of_dicts)

print(type(trans_list_of_dicts))
print((trans_list_of_dicts[0].keys()))
for item in trans_list_of_dicts:
    print(item.get("InvoiceNo"))

for item in trans_list_of_dicts:
    if item.get('InvoiceNo') == 536370:
        print(item)

update_dict ={
    "InvoiceNo": 1,
    "StockCode": 1,
    "Description": "MINI PAINT SET VINTAGE",
    "Quantity": 1,
    "InvoiceDate": "12/1/2010 8:45",
    "UnitPrice": 0.65,
    "CustomerID": 1,
    "Country": "France"

}

for item in trans_list_of_dicts:
    if item.get("InvoiceNo") == 536370:
        item.update(update_dict)
        print(item)
with open("/Users/lionel/PyCharmMiscProject/jsn.json", 'w') as json_file:
    json.dump(trans_list_of_dicts, json_file)
