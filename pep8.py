def parar():
    """Funcion para parar el programa en cada una de las opciones."""
    input("Presione <ENTER> para continuar")


def capturar():
    """Permite capturar la temperatura ingresada por el usuario."""
    try:
        temperatura = float(input("Por favor digite la temperatura: "))
        return temperatura
    except ValueError as e:
        print(f"Error: {e}")


def celsius_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def celsius_kelvin(celsius):
    """Convierte grados Celsius a Kelvin."""
    return celsius + 273.15


def kelvin_fahrenheit(kelvin):
    """Convierte grados Kelvin a Fahrenheit."""
    return (kelvin - 273.15) * 9 / 5 + 32


def kelvin_celsius(kelvin):
    """Convierte grados Kelvin a Celsius."""
    return kelvin - 273.15


def fahrenheit_kelvin(fahrenheit):
    """Convierte grados Fahrenheit a Kelvin."""
    return (fahrenheit - 32) * 5 / 9 + 273.15


def fahrenheit_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    """Funcion principal que ejecuta el menu interactivo."""
    try:
        continuar = True
        temperatura = 0.0

        menu = (
            "Seleccione una opcion:\n"
            "1 --> Capturar Temperatura\n"
            "2 --> Celsius a Fahrenheit\n"
            "3 --> Celsius a Kelvin\n"
            "4 --> Kelvin a Fahrenheit\n"
            "5 --> Kelvin a Celsius\n"
            "6 --> Fahrenheit a Kelvin\n"
            "7 --> Fahrenheit a Celsius\n"
            "0 --> Salir"
        )

        while continuar:
            opcion = input(menu + "\n")

            if opcion == "1":
                temperatura = capturar()
            elif opcion == "2":
                print(f"{temperatura}°C = {celsius_fahrenheit(temperatura)} °F")
                parar()
            elif opcion == "3":
                print(f"{temperatura}°C = {celsius_kelvin(temperatura)} °K")
                parar()
            elif opcion == "4":
                print(f"{temperatura}°K = {kelvin_fahrenheit(temperatura)} °F")
                parar()
            elif opcion == "5":
                print(f"{temperatura}°K = {kelvin_celsius(temperatura)} °C")
                parar()
            elif opcion == "6":
                print(f"{temperatura}°F = {fahrenheit_kelvin(temperatura)} °K")
                parar()
            elif opcion == "7":
                print(f"{temperatura}°F = {fahrenheit_celsius(temperatura)} °C")
                parar()
            elif opcion == "0":
                print("Bye bye Hasta luego")
                continuar = False
            else:
                print("Seleccione una opcian valida")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")


if _name_ == "_main_":
    main