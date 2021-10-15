# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:09:03 2021

@Created by: David
"""
from PrintFunctions import printMessage
from Ship import Ship
import re

class Player:
    
    
    
    def __init__(self, name,coordinates, sizeBoard):
        self.name = name
        self.coordinates = coordinates
        self.sizeBoard = sizeBoard
        self.mapping_coordinates = {}
        self.valid_positions = {}
        self.ship = Ship()
    
    
#    def set_ship_coodinates(self, ship, coordinates):
#        if self.mapping_coordinates.get(ship,0) == 0:
#            self.mapping_coordinates[ship] = [coordinates]
#        else:
#            self.mapping_coordinates.update(ship = self.mapping_coordinates[ship] + coordinates)
    
    def set_coordiantes(self, ship, dictionary, coordinates = 0):
        if dictionary.get(ship,0) == 0:
            dictionary[ship] = [coordinates]
        else:
            dictionary.update(ship = self.dictionary[ship] + coordinates)
        return dictionary
        
    
    def input_coordinates(self, ship, sizeBoard):
        printMessage("las coodenadas tienen que estar separadas con comas")
        printMessage(""*27+"x y")
        ship_coordinates = input("Cuales coordenadas eliges: ")  
        if sizeBoard < 10:
            if bool(re.search(rf"^[A-Za-z],[0-{sizeBoard}]$", ship_coordinates)):
                print("llegue")
                self.ship.add_coodenates(ship,ship_coordinates.split(','))
        else:
            if bool(re.search(rf"^[0-1][0-{sizeBoard - 10}],[0-1][0-{sizeBoard - 10}]$", ship_coordinates)):
                pass
        return 
        
        