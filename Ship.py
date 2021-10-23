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
        #agregan coordenadas alos diccionarios
        def add_process(self, ship, ship_coordinates,boatSize):
            if boatSize.get(ship_coordinates[0].upper(),0) == 0: # no existe
                boatSize[ship_coordinates[0].upper()] = ship_coordinates[1]
            else:
                list_new = list(boatSize.get(ship_coordinates[0].upper()))
                list_new.append(ship_coordinates[1])
                boatSize[ship_coordinates[0].upper()] = list_new
        #validamos que llave se uso para agregar coordenadas al diccionario
        if ship == self.big_ship_key:
            add_process(self, ship, ship_coordinates,self.big_ship)
        elif ship == self.medium_ship_key:
            add_process(self, ship, ship_coordinates,self.medium_ship)
        else:
            add_process(self, ship, ship_coordinates,self.small_ship)
        
    
    
    def is_full(self, ship, HumanPlayer):
        '''Check if ship is already full or there is a field that needs to be populated'''
        count = 0
        ship_items = {}
        if ship == self.big_ship_key:
            ship_items = HumanPlayer.ship.big_ship.items()
        elif ship == self.medium_ship_key:
            ship_items = HumanPlayer.ship.medium_ship.items()
        elif ship == self.small_ship_key:
            ship_items = HumanPlayer.ship.small_ship.items()
            
        for key, value in ship_items:
            if isinstance(value, list):
                count += len(value)
            else:
                count+=1
        if count == self.max_positions[ship]:
            return True
        return False
            