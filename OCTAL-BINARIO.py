def octal_a_decimal(octal):
    print(f"Convirtiendo el octal {octal}...")
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    octal = octal[::-1]
    for digito in octal:
        print(f"El número decimal es {decimal}")
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        print(
            f"Elevamos el 8 a la potencia {posicion} (el resultado es {numero_elevado}) y multiplicamos por el carácter actual: {valor_entero}")
        decimal += equivalencia
        print(f"Sumamos {equivalencia} a decimal. Ahora es {decimal}")
        posicion += 1
    return decimal
octal = input("Ingresa un número octal: ")
decimal = octal_a_decimal(octal)
print(f"El octal {octal} es {decimal} en decimal")
