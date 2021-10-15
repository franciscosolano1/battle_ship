# -*- coding: utf-8 -*-
"""
    Main source

"""
import sys
import re
sys.path.append(".")
from Player import Player
from Ship import Ship



def printMessage( *message,  delimiter = None, matrix = None):
    if delimiter != None:
        print(delimiter)
    for mes in message:
        if matrix != None: # si es una matriz que la muestre con forma
            for mat in mes:
                print(mat)
        else:               # si no es matriz que muestre los argumentos
            print(mes)
    if delimiter != None:
        print(delimiter)


###################### Validación del nombre ######################

sizeBoard = 0
player_name = ""
Ship_to_be_selected = ""
print("+"*60)
print("¡Bienvenido a Battleship rupestre!")
print("+"*60)

###################### Name Validation ######################

while player_name == "":
    player_name = input("Cual es tu nombre:").capitalize()
    if not bool(re.search(r"^[A-Za-z]{3,}$", player_name)):
        printMessage("\t \t Error: solo acepta más de 3 letras, no acepta algun otro caracter", delimiter = "- " * 40)
        player_name = ""
        
###################### Size board Validation ######################

while sizeBoard < 7 or sizeBoard > 14:
    try:
        printMessage("\t \t Definamos el tamaño del tablero, no puede ser menor a 7 ni mayor a 14", delimiter ="")
        sizeBoard = int(input("Ingrese el valor del tablero: "))
        if sizeBoard < 7 or sizeBoard > 14:
            printMessage("\t \t WARNING! = ¡Revisa las instrucciones!", delimiter="")
    except ValueError:
        printMessage("No se ha ingresado un número, vuelve a intentar")

###################### Assigning Coordinates ######################

printMessage(f"\t \t ¡Perfecto {player_name}! ahora definamos las reglas y las coordenadas donde quieres posicionar tus barcos", delimiter ="")

printMessage("= Reglas","= Puedes agregar los siguientes barcos:"
             ,"= \t \t a. 1 Barco Grande (ocupa 6 espacios)"
             ,"= \t \t b. 1 Barco Mediano (ocupa 4 posiciones)"
             ,"= \t \t c. 3 Barcos Pequeños (Ocupa 2 posiciones)"
             ,"="
             ,"= Deberas seleccionar cual barco quieres crear y en seguida que posiciones ira, solo se permite de manera Horizontal o vertical, no importa el orden en que los elijas "
             ,"="
             ,delimiter = "="*120
             )

HumanPlayer = Player(player_name,[],sizeBoard) 

# filling matriz with 0 values in each position
for i in range(sizeBoard):
   HumanPlayer.coordinates.append([0 for j in range(sizeBoard)])


printMessage("Cada valor de 0 es una posicion a la que puedes asignar una parte de cada barco")
printMessage("Tu tablero:")
printMessage(HumanPlayer.coordinates,delimiter=None,matrix=1)



while Ship_to_be_selected == "":    
    Ship_to_be_selected = input("Cual Barco te gustaría utilizar:")
    if Ship_to_be_selected == "a":
        printMessage("las coodenadas tienen que estar separadas con comas")
        ship_coordinates = input("Cuales coordenadas eliges: ")
        #HumanPlayer.set_ship_coodinates(Ship_to_be_selected, ship_coordinates.split())
        HumanPlayer.input_coordinates(Ship_to_be_selected)
    elif Ship_to_be_selected == "b":
        pass
    elif Ship_to_be_selected == "c":
        pass
    else:
        pass



 
 
#p1 = Player("David",[[1,2,3,4,5],[6,7,8,9,0]], 3) 

#print()





