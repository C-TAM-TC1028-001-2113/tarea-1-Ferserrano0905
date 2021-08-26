def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))

    paginas = palabras / 475
    des = (paginas * 60) * .10
    costo = des * 60

    print("El costo de la publicación es: ", costo)


if __name__ == '__main__':
    main()
