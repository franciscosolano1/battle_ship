# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:09:03 2021

@Created by: David
"""
from PrintFunctions import printMessage
from Ship import Ship
from random import randint
import random
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
        
        
        ship_coordinates = input("Cuales coordenadas eliges: ")  #input coordinates
        if sizeBoard < 10: #checking sizeBoard since cannot put both validation together in a regex
            if bool(re.search(rf"^[A-Za-z],[0-{sizeBoard}]$", ship_coordinates)):
                #validation to check if a value had been populated
                if self.check_positions_taken(ship_coordinates.split(','), self.ship.big_ship) or self.check_positions_taken(ship_coordinates.split(','), self.ship.medium_ship) or self.check_positions_taken(ship_coordinates.split(','), self.ship.small_ship):
                    printMessage("Esa posición ya ha sido tomada, intenta con otra")
                else: # adding unique coordinates
                    self.ship.add_coodenates(ship,ship_coordinates.upper().split(','))
                    # add position in matrix coordinates
                    self.coordinates[int(ship_coordinates.split(",")[1])][ord(ship_coordinates.upper().split(",")[0])-65] = 1
        else:
            if bool(re.search(rf"^[0-1][0-{sizeBoard - 10}],[0-1][0-{sizeBoard - 10}]$", ship_coordinates)):
                pass
              
    def automatic_generation(self, sizeBoard):
        vertial_or_horizontal = randint(0, 1) #0 -  horizontal, 1 - vertical
        column_to_start = randint(0, sizeBoard-1)
        
        #big_ship
        random_start = randint(0,sizeBoard-self.ship.max_positions[self.ship.big_ship_key])
        coordinates = chr(column_to_start+65)+","+str(random_start)
        for i in range(0,6):
            self.ship.add_coodenates(self.ship.big_ship_key,coordinates.split(","))
            self.coordinates[int(coordinates.split(",")[1])][ord(coordinates.split(",")[0])-65] = 1
            if vertial_or_horizontal == 0:
                random_start = random_start + 1
            else:
                column_to_start = column_to_start + 1
            coordinates = chr(column_to_start+65)+","+str(random_start)
        
        #medium_ship
        
        sample_list = random.sample(range(sizeBoard),k=sizeBoard)
        
        for row in sample_list:
            count_empty_space = 0;
            for value in range(0,len(self.coordinates[row])):
                if self.coordinates[row][value] == 0:
                    count_empty_space = count_empty_space + 1
                else:
                    count_empty_space = 0
                
                if count_empty_space == 4:
                    print(f"encontre 4 posiciones vacias en {row} y {value}")
                    self.coordinates[row][value] = 1
                    self.ship.add_coodenates(self.ship.medium_ship_key,[chr(row+65), str(value)])
                    self.coordinates[row][value-1] = 1
                    self.ship.add_coodenates(self.ship.medium_ship_key,[chr(row+65), str(value-1)])
                    self.coordinates[row][value-2] = 1
                    self.ship.add_coodenates(self.ship.medium_ship_key,[chr(row+65), str(value-2)])
                    self.coordinates[row][value-3] = 1
                    self.ship.add_coodenates(self.ship.medium_ship_key,[chr(row+65), str(value-3)])
                    
                    break
            if count_empty_space == 4:
                break
        
        #small
        sample_list = random.sample(range(sizeBoard),k=sizeBoard)
        for row in sample_list:
            count_empty_space = 0;
            for value in range(0,len(self.coordinates[row])):
                if self.coordinates[row][value] == 0:
                    count_empty_space = count_empty_space + 1
                else:
                    count_empty_space = 0
                
                if count_empty_space == 2:
                    print(f"encontre 4 posiciones vacias en {row} y {value}")
                    self.coordinates[row][value] = 1
                    self.ship.add_coodenates(self.ship.small_ship_key,[chr(row+65), str(value)])
                    self.coordinates[row][value-1] = 1
                    self.ship.add_coodenates(self.ship.small_ship_key,[chr(row+65), str(value-1)])
                    break
            if count_empty_space == 2:
                break
                    

HumanPlayer= {"A":[1,2,3]}
shoot=["A",1]
def hits(self,HumanPlayer,shoot):
    for key, value in HumanPlayer:
        if key == shoot[0]:
            if isinstance(value, list):
                if shoot[1] in value:
                    value_return = True
                    HumanPlayer
                    print("t")
                    break
                else:
                    if ship_coordinates[1] == value:
                        value_return = True
                        break

