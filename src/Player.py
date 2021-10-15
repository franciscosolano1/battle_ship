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
    
    
    def set_coordiantes(self, ship, dictionary, coordinates = 0):
        if dictionary.get(ship,0) == 0:
            dictionary[ship] = [coordinates]
        else:
            dictionary.update(ship = self.dictionary[ship] + coordinates)
        return dictionary
        
    
    def check_positions_taken(self, ship_coordinates, ship_dictionary):
        value_return = False
        for key, value in ship_dictionary.items():
            if key == ship_coordinates[0]:
                
                if isinstance(value, list):
                    if ship_coordinates[1] in value:
                        value_return = True
                        break
                else:
                    if ship_coordinates[1] == value:
                        value_return = True
                        break
        
        return value_return
    
    def input_coordinates(self, ship, sizeBoard):
        '''Start populating all coordinates per ship if it is possible'''
        
        printMessage("las coodenadas tienen que estar separadas con comas")
        printMessage(""*27+"x y")
        ship_coordinates = input("Cuales coordenadas eliges: ")  #input coordinates
        if sizeBoard < 10: #checking sizeBoard since cannot put both validation together in a regex
            if bool(re.search(rf"^[A-Za-z],[0-{sizeBoard}]$", ship_coordinates)):
                #validation to check if a value had been populated
                if self.check_positions_taken(ship_coordinates.split(','), self.ship.big_ship) or self.check_positions_taken(ship_coordinates.split(','), self.ship.medium_ship) or self.check_positions_taken(ship_coordinates.split(','), self.ship.small_ship):
                    printMessage("Esa posición ya ha sido tomada, intenta con otra")
                else: # adding unique coordinates
                    self.ship.add_coodenates(ship,ship_coordinates.split(','))
        else:
            if bool(re.search(rf"^[0-1][0-{sizeBoard - 10}],[0-1][0-{sizeBoard - 10}]$", ship_coordinates)):
                pass
        