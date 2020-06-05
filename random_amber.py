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
        self.all_connections = connections_object.connections
        self.used_connections = []
        self.trajects = []
        self.max_trajects = 7
        self.max_time = 120
        self.total_time = 0
        self.total_trajects = 0
        
    def find_traject(self):
        for i in range(self.max_trajects):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            traject = [start_city]
            
            print("start:", start_city.name, time, traject)
            
            while time < self.max_time:
                neighbours = start_city.get_neighbours()
                #neighbours = self.check_traject(start_city, neighbours)
                random_val = random.randint(0, len(neighbours) - 1)
                next_city = neighbours[random_val]
                traject.append(next_city)
                time += start_city.get_time(next_city)
            
                #self.used_connections.append([start_city, next_city])
                
                start_city = next_city
                
                print("next:", next_city.name, time, traject)
                print("used:", self.used_connections)
            
            self.trajects.append(traject)
            self.total_time += time
            
            print("end:", self.total_time, self.trajects)
            self.total_trajects += 1
        
        
    def check_traject(self, city, neighbours):
        if city in self.used_connections:
            pass
        return neighbours
    
    def score(self):
        p = len(self.used_connections) / len(self.total_connections)
        return p * 10000 - (self.total_trajects * 100 + self.total_time)
        

if __name__ == "__main__":
    # Run the connections class with the connections file
    #connections = Connections("data/ConnectiesHolland.csv")
    #test = Random(connections).find_traject()
    
    string1 = "Amsterdam"
    string2 = "Almere"
    
    listi = [["Amsterdam", "Almere"]]
    new = [string2, string1]
    new.sort()
    print(new)
    if new in listi:
        print(new)