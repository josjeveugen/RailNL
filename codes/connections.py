# City is een soort node object.
# De node staat voor een stad, het houdt bij welke buren deze heeft
# en hoelang het duurt om een buur te bereiken.
import csv

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
                return float(self.times[i])
            i += 1
        return None 
            
    def get_neighbours(self):
        return self.neighbours

class Connections(object):
    def __init__(self, connections_file):
        self.cities = []
        self.city_ids = {}
        self.connections = []
        # loading the cities into self.cities and city_ids
        self.load_cities(connections_file)


    def load_cities(self, connections_file):
        with open(connections_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                city1 = row["station1"]
                city2 = row["station2"]
                # sorting in alphabetical order
                city_pair = [city1, city2]
                city_pair.sort()
                time = row["distance"]
                city_pair.append(float(time))

                self.connections.append(city_pair)

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
        return self.connections
