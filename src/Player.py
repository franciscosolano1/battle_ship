# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:09:03 2021

@Created by: David
"""
from Battleship import printMessage

class Player:
    
    
    
    def __init__(self, name,coordinates, sizeBoard):
        self.name = name
        self.coordinates = coordinates
        self.sizeBoard = sizeBoard
        self.mapping_coordinates = {}
        self.valid_positions = {}
    
    
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
        
    
    def input_coordinates(self, ship):
        self.valid_positions = self.set_coordiantes(ship, self.valid_positions,1)
        printMessage("las coodenadas tienen que estar separadas con comas")
        printMessage(""*27+"x y")
        
        