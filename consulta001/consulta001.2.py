while True:
    edad_str = input("Por favor, ingresa tu edad: ")

    if edad_str.isdigit():
        edad = int(edad_str)
        print("Tu edad es:", edad)
        break
    else:
        print("Por favor, ingresa un número válido para la edad.")