# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:59:42 2021

@author: David
"""

class Ship:
    
    def __init__(self):
        self.big_ship_key = "a"
        self.medium_ship_key = "b"
        self.small_ship_key = "c"
        self.valid_number_ship = {self.big_ship_key:1,self.medium_ship_key:1,self.small_ship_key:3}
        self.max_positions = {self.big_ship_key:6,self.medium_ship_key:4,self.small_ship_key:2}
        self.big_ship = {}
        self.medium_ship = {}
        self.small_ship = {}
     
    def add_coodenates(self, ship, ship_coordinates):
        if ship == self.big_ship_key:
            if self.big_ship.get(ship_coordinates[0].upper(),0) == 0: # no existe
                self.big_ship[ship_coordinates[0].upper()] = ship_coordinates[1]
            else:
                list_new = list(self.big_ship.get(ship_coordinates[0].upper()))
                list_new.append(ship_coordinates[1])
                self.big_ship[ship_coordinates[0].upper()] = list_new
        elif ship == self.medium_ship_key:
            if self.medium_ship.get(ship_coordinates[0].upper(),0) == 0: # no existe
                self.medium_ship[ship_coordinates[0].upper()] = ship_coordinates[1]
            else:
                list_new = list(self.medium_ship.get(ship_coordinates[0].upper()))
                list_new.append(ship_coordinates[1])
                self.medium_ship[ship_coordinates[0].upper()] = list_new
        else:
            if self.small_ship.get(ship_coordinates[0].upper(),0) == 0: # no existe
                self.small_ship[ship_coordinates[0].upper()] = ship_coordinates[1]
            else:
                list_new = list(self.small_ship.get(ship_coordinates[0].upper()))
                list_new.append(ship_coordinates[1])
                self.small_ship[ship_coordinates[0].upper()] = list_new
    
    
    
    def is_full(self, ship, HumanPlayer):
        count = 0
        for key, value in HumanPlayer.ship.big_ship.items():
            if isinstance(value, list):
                count += len(value)
            else:
                count+=1
        if count == self.max_positions[ship]:
            return True
        return False
            