
listaNotas = [10, 8, 7 , 5 ,9]


def calcular_media(listaNotas):
    media = 0
    for n in listaNotas:
        media = sum(listaNotas)
    return media/len(listaNotas)

print(calcular_media(listaNotas))


def verificar_situacao(media):
    