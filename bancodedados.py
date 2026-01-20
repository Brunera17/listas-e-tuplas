cidade1 = ("São Paulo", -23.5505, -46.6333)
cidade2 = ("Rio de Janeiro", -22.9065, -43.1729)
cidade3 = ("Brasília", -15.7801, -47.9292)

cidades = [cidade1, cidade2, cidade3]

for cidade in cidades:
    nome, latitude, longitude = cidade
    print(f"Cidade: {nome}, Latitude: {latitude}, Longitude: {longitude}")