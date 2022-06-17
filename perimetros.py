def perimetro_cuadrado():
    lado = float(input("Ingrese el valor del lado "))
    return print("El perimetro del cuadrado es",lado*4)

def perimetro_circulo():
    radio = float(input("Ingrese el valor del radio "))
    pi = 3.1416
    return print("El perimetro del circulo es",2*pi*radio)

def perimetro_rectangulo():
    largo = float(input("Ingrese el valor del largo "))
    ancho = float(input("Ingrese el valor del ancho "))
    return print("El perimetro del rectangulo es",(2*largo) + (2*ancho))

if __name__==("__main__"):
    print(__name__)
    print("Yo soy la funcion principal")
    perimetro_cuadrado()
    perimetro_rectangulo()
    perimetro_circulo()
else:
    print("No soy la funcion principal, soy un modulo")
    print(__name__)