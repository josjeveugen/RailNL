#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:21:31 2020

@author: ambercok
"""

from connections import City
from connections import Connections
import random

class Random(object):
    def __init__(self, connections_object):
        self.cities = connections_object.cities
        self.ids = connections_object.city_ids
        self.connections = connections_object.connections
        self.trajects = []
        self.max_trajects = 7
        self.max_time = 120
        
    def find_trajects(self):
        start = random.randint(0, len(self.cities) - 1)
        print(start)
        start_city = self.cities[start]
        
        print(start_city.name)
        

if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")
    test = Random(connections).find_trajects()