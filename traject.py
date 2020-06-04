# City is een soort node object.
# De node staat voor een stad, het houdt bij welke buren deze heeft
# en hoelang het duurt om een buur te bereiken.
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
        for value in neighbours:
            if value == city: # check of dit zo kan?
                return self.time[i]
            i += 1

class Connections(object):
    def __init__(self, connections = []):
        self.nodes = []
        self.ids = {}

        self.load_nodes(connections)

    def load_nodes(self, connections):
        for connection in connections:
            city1 = connection[0]
            city2 = connection[1]
            time = connection[2]

            if city1 not in self.ids:
                self.nodes.append(City(city1))
                self.ids[city1] = len(self.ids)

            if city2 not in self.ids:
                self.nodes.append(City(city2))
                self.ids[city2] = len(self.ids)

            city_node1 = self.nodes[self.ids[city1]]
            city_node2 = self.nodes[self.ids[city2]]
            city_node1.add_neighbour(city_node2, time)
            city_node2.add_neighbour(city_node1, time)



if __name__ == "__main__":
    connections = [["adam", "eindhoven", 5], ["adam", "utrecht", 10], ["adam", "urk", 9]]
    test = Connections(connections)
