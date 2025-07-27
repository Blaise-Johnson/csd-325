import requests

#Call the Pokémon TCG API
response = requests.get("https://api.pokemontcg.io/v2/cards?q=name:squirtle")

#Prints status 
print(response.status_code)

# Prints unformatted Json
print(response.json())

#Prints formatted 
if response.status_code == 200:
    data = response.json()
    print("\nFormatted Pokémon Card Data:\n")
    for card in data['data'][:3]:  
        print(f"Name: {card['name']}")
        print(f"Set: {card['set']['name']}")
        print(f"Image URL: {card['images']['small']}")
        print("---")
else:
    print("Failed to retrieve data.")
