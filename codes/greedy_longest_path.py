from .connections import *
import random
import csv

# Algorithm that chooses the neighbour with the shortest travel time
class Algorithm(object):
    def __init__(self, args):
        self.ids = args[0].city_ids
        self.all_connections = args[0].connections
        self.trajects = []
        self.used_connections = []
        self.max_time = args[1]
        self.max_trajects = args[2]
        self.total_time = 0

    def find_traject(self):
        for i in range(self.max_trajects):
            # Choose a random city to start with
            current_city = random.choice(list(self.ids.keys()))
            self.time = 0
            self.traject = [current_city]
            last_city = ""

            while True:
                possible_connections = []
                for connection in self.all_connections:
                    if current_city in connection:
                        possible_connections.append(connection)

                # Make sure going back to the station you came from is no option
                for connection in possible_connections:
                    if last_city in connection:
                        possible_connections.remove(connection)
                if not possible_connections:
                    break

                possible_connections.sort(key=lambda x: x[2])
                short_connection = possible_connections[0]

                for i in range(len(possible_connections)):
                    if possible_connections[i] not in self.used_connections:
                        short_connection = possible_connections[i]
                        break

                if self.time + int(short_connection[2]) > self.max_time:
                    break

                # If connection's not yet in the connections_added list, add it
                if short_connection not in self.used_connections:
                    self.used_connections.append(short_connection)

                self.time += int(short_connection[2])
                last_city = current_city
                if current_city == short_connection[1]:
                    current_city = short_connection[0]
                elif current_city in short_connection[0]:
                    current_city = short_connection[1]
                self.traject.append(current_city)

            self.trajects.append(self.traject)
            self.total_time += self.time

            if len(self.used_connections) == len(self.all_connections):
                return self.score(), self.trajects, self.used_connections, self.total_time

        return self.score(), self.trajects, self.used_connections, self.total_time

    # Calculate score
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        return p * 10000 - (len(self.trajects) * 100 + self.total_time)