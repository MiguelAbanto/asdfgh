meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'SHEESH': 'ligera desaprobación',
            'CREEPY': 'aterrador, siniestro',
            'ROFL': 'ligera desaprobación',
            'AGGRO': 'ponerse agresivo/enojado',
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('la palabra no se encontro')
