import math


def main():
    # escribe tu código abajo de esta líne
    palabras = int(input("Dame el número de palabras: "))

    paginas = math.ceil(palabras / 475)
    des = (paginas * 60) * .10
    costo = (paginas * 60) - des

    print("El costo de la publicación es: ", costo)


if __name__ == '__main__':
    main()
