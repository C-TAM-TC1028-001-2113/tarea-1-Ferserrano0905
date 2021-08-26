def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))

    dif = (saldo + ingresos) - egresos - (13 * cheques)
    interes = dif * 0.075
    total = dif - interes

    print("El saldo final de la cuenta es: ", total)


if __name__ == '__main__':
    main()
