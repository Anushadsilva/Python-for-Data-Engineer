import requests
ROOT_URL = "https://api.disneyapi.dev"

#
response = requests.get(f"{ROOT_URL}/character")
print(response.status_code)
print(response.json())

print(response.headers)

disney_data = response.json()
print(disney_data.keys())
print(disney_data["info"])

print(disney_data["data"])

print(len(disney_data["data"]))

response = requests.get(disney_data["info"]["nextPage"])


parms = {"page": 4, "pageSize": 4}

res = requests.get(f"{ROOT_URL}/character", params=parms)
characters_from_page_4_with_20_characters = res.json()
print(characters_from_page_4_with_20_characters)
print(res.url)

print(characters_from_page_4_with_20_characters["info"])
print(characters_from_page_4_with_20_characters["data"])
print(len(characters_from_page_4_with_20_characters["data"][0].keys()))
print(characters_from_page_4_with_20_characters["data"][0].keys())

characters = [
    {"id":characters["_id"] , "name":characters["name"]}
    for characters in characters_from_page_4_with_20_characters["data"]
]
print(characters)


charater_id = 156
response1 = requests.get(f"{ROOT_URL}/character/{charater_id}")
character_156 =response1.json()["data"]
print(character_156)


