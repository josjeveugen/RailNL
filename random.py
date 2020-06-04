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
        # ?? How to link the neighbours to the ID of the city??
        for city in self.neighbours:
            print(city.name)
        print(self.times)
        print("\n")


    def get_time(self, city):
        i = 0
        for value in neighbours:
            if value == city: # check of dit zo kan?
                return self.time[i]
            i += 1



class Connections(object):
    def __init__(self, connections = []):
        self.nodes = []
        self.ids = {}
        self.load_nodes(connections)


    def load_nodes(self, connections_file):
        # the list that contains all the connections
        connections = []
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
                connections.append(neighbours)

                if city1 not in self.ids:
                    self.nodes.append(City(city1))
                    self.ids[city1] = len(self.ids)

                if city2 not in self.ids:
                    self.nodes.append(City(city2))
                    self.ids[city2] = len(self.ids)

                # The prints are for testing purposes
                city_node1 = self.nodes[self.ids[city1]]
                city_node2 = self.nodes[self.ids[city2]]
                print(self.ids[city1])
                city_node1.add_neighbour(city_node2, time)
                print(self.ids[city2])
                city_node2.add_neighbour(city_node1, time)

        # Testing print
        print(self.ids)


if __name__ == "__main__":
    # Run the connections function with the connections file
    test = Connections("data/ConnectiesHolland.csv")

