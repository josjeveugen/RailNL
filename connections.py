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

        # for testing purposes in the terminal
        # Show all the city's neighbours and then their travel duration
        for city in self.neighbours:
            print(city.name)
        print(self.times)
        print("\n")


    def get_time(self, city):
        i = 0
        for city_node in self.neighbours:
            if city_node == city: # check of dit zo kan?
                return self.times[i]
            i += 1


class Connections(object):
    def __init__(self, connections = []):
        self.cities = []
        self.city_ids = {}
        self.connections = []
        # loading the cities into self.cities and city_ids
        self.load_cities(connections)
        

    def load_cities(self, connections_file):
        with open(connections_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                city1 = row["station1"]
                city2 = row["station2"]
                time = row["distance"]

                self.connections.append([city1, city2, time])

                if city1 not in self.city_ids:
                    self.cities.append(City(city1))
                    self.city_ids[city1] = len(self.city_ids)

                if city2 not in self.city_ids:
                    self.cities.append(City(city2))
                    self.city_ids[city2] = len(self.city_ids)

                # The prints are for testing purposes
                city_node1 = self.cities[self.city_ids[city1]]
                city_node2 = self.cities[self.city_ids[city2]]

                # Print the ID of the city
                print(self.city_ids[city1])
                city_node1.add_neighbour(city_node2, time)
                print(self.city_ids[city2])
                city_node2.add_neighbour(city_node1, time)

        # Testing print all the cities with their ID
        print(self.city_ids)


if __name__ == "__main__":
    # Run the connections class with the connections file
    test = Connections("data/ConnectiesHolland.csv")

