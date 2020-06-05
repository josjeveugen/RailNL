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
        
        print(self.all_connections)
        
    def find_traject(self):
        for i in range(self.max_trajects):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            under_timelimit = True
            traject = [start_city]
            
            print("start:", start_city.name, time, traject)
            
            while under_timelimit:
                # checkt of alle mogelijke verbindingen al zijn gemaakt.
                if len(self.used_connections) == len(self.all_connections):
                    return self.score()
                
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)
                random_val = random.randint(0, len(neighbours) - 1)
                next_city = neighbours[random_val]
                traject.append(next_city)
                next_time = start_city.get_time(next_city)
                
                # check of niet over limit gaat
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                time += next_time
                
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)
                else:
                    print("double")
                
                start_city = next_city

            self.trajects.append(traject)
            self.total_time += time
            self.total_trajects += 1
            
        return self.score()
        
        
    def check_traject(self, city, neighbours):
        new_neigh = []
        for neighbour in neighbours:
            city_pair = [city.name, neighbour.name]
            city_pair.sort()
            if city_pair not in self.used_connections:
                new_neigh.append(neighbour)
        
        if new_neigh == []:
            print("all neighbours are already used")
            return neighbours
        return new_neigh
    
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        print(len(self.used_connections), len(self.all_connections), self.used_connections)
        print(p, self.total_trajects, self.total_time)
        return p * 10000 - (self.total_trajects * 100 + self.total_time)
        

if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")
    test = Random(connections).find_traject()
    print(test)
