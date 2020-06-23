from .connections import City
from .connections import Connections
import random
import csv


# Algorithm that chooses a random neighbour
class Algorithm(object):
    def __init__(self, args):
        self.cities = args[0].cities
        self.ids = args[0].city_ids
        self.all_connections = args[0].connections
        self.used_connections = []
        self.trajects = []
        self.max_trajects = args[2]
        self.max_time = args[1]
        self.total_time = 0

    def find_traject(self):
        for i in range(self.max_trajects):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            # This is used to check whether the traject has exceeded the time limit
            under_timelimit = True
            traject = [start_city.name]

            while under_timelimit:
                # Checks the possible neighbours and if they have been used already
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)

                # Pick a random neighbour
                random_val = random.randint(0, len(neighbours) - 1)
                next_city = neighbours[random_val]
                next_time = start_city.get_time(next_city)

                # Start new traject if time limit has been exceeded
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                traject.append(next_city.name)
                time += next_time

                # Add new city to used_connections
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)

                start_city = next_city

            self.trajects.append(traject)
            self.total_time += time

        return self.score(), self.trajects, self.used_connections, self.total_time

    # Checks if the neighbours have been used already
    def check_traject(self, city, neighbours):
        new_neigh = []
        for neighbour in neighbours:
            city_pair = [city.name, neighbour.name]
            city_pair.sort()
            if city_pair not in self.used_connections:
                new_neigh.append(neighbour)

        # If all neighbours are already used, return all possible neighbours
        if new_neigh == []:
            return neighbours
        return new_neigh

    # Calculate score
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        return p * 10000 - (len(self.trajects) * 100 + self.total_time)