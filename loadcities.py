# City is een soort node object.
# De node staat voor een stad, het houdt bij welke buren deze heeft
# en hoelang het duurt om een buur te bereiken.
import csv
from random_julia import *

class City(object):
    def __init__(self, identity):
        self.name = identity
        # neighbours is een lijst met de verbonden city_nodes
        self.neighbours = []
        # dit houdt de tijden bij (de tijd op index 0 is de tijd van de city
        # op index 0 van neighbours)
        self.times = []

    # voeg een verbonden stad toe die ook een node is
    def add_neighbour(self, neighbour, time):
        self.neighbours.append(neighbour)
        self.times.append(time)

    def get_time(self, city):
        i = 0
        for value in self.neighbours:
            if value == city:  # check of dit zo kan?
                return self.times[i]
            i += 1

class Connections(object):
    def __init__(self, connections):
        self.cities = []
        self.city_ids = {}
        self.load_cities(connections)

    def load_cities(self, connections_file):
        # the list that contains all the connections
        self.all_connections = []
        with open(connections_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # the list with every neighbour for an individual city
                neighbours = []
                city1 = row["station1"]
                city2 = row["station2"]
                time = row["distance"]

                # Add the neighbours to the list of the city
                neighbours.append(city1)
                neighbours.append(city2)
                neighbours.append(time)
                self.all_connections.append(neighbours)

                if city1 not in self.city_ids:
                    self.cities.append(City(city1))
                    self.city_ids[city1] = len(self.city_ids)

                if city2 not in self.city_ids:
                    self.cities.append(City(city2))
                    self.city_ids[city2] = len(self.city_ids)

                city_node1 = self.cities[self.city_ids[city1]]
                city_node2 = self.cities[self.city_ids[city2]]

                city_node1.add_neighbour(city_node2, time)
                city_node2.add_neighbour(city_node1, time)

    # Get all locations
    def get_locations(self):
        return self.city_ids

    # Get all the connections
    def get_all_connections(self):
        return self.all_connections

    # Get the neighbours from a specific station
    def get_neighbours(self, current_station):
        possible_locations = []
        for city in self.all_connections:
            if city[0] == current_station:
                possible_locations.append(city)

            elif city[1] == current_station:
                possible_locations.append(city)

        return possible_locations


if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")
    all_locations = connections.get_locations()
    all_connections = connections.get_all_connections()
    random_outcome(connections, all_locations, all_connections)
