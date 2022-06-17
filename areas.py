def area_cuadrado():
    lado = float(input("Ingrese el valor del lado "))
    return print("El área del cuadrado es",lado**2)

def area_circulo():
    radio = float(input("Ingrese el valor del radio "))
    pi = 3.1416
    return print("El área del circulo es",pi*(radio**2))

def area_rectangulo():
    largo = float(input("Ingrese el valor del largo "))
    ancho = float(input("Ingrese el valor del ancho "))
    return print("El área del rectangulo es",largo * ancho)

if __name__==("__main__"):
    print(__name__)
    print("Yo soy la funcion principal")
    area_cuadrado()
else:
    print("No soy la funcion principal, soy un modulo")
    print(__name__)