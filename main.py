from areas import *
from perimetros import perimetro_circulo, perimetro_cuadrado, perimetro_rectangulo

def main():
    print("--"*20)
    print("Calculo de figuras")
    print("--"*20)
    
    figura = input("Nombre de la figura ")
    
    if(figura == "circulo"):
        area_circulo()
        perimetro_circulo()
    elif(figura == "cuadrado"):
        area_cuadrado()
        perimetro_cuadrado()
    elif(figura == "rectangulo"):
        area_rectangulo()
        perimetro_rectangulo()
    else:
        print("No se encontró la figura")

if __name__==("__main__"):
    main()
        