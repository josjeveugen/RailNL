import random
from connections import *
import csv

# Function that prints a random 'lijnvoering'
class Trainroutes(object):
    # Create object that holds all the trajects
    def __init__(self, connections, locations, all_connections):
        # This list holds all the trajects
        self.all_routes = []
        self.total_connections = all_connections
        self.locations = locations
        self.already_visited = []
        self.total_duration = 0
        self.num_trajecten = 7
        self.time_limit = 120

    def add_trajects(self):
        i = 0
        # Keep creating trajects until the max amount of traject is reached
        while i < self.num_trajecten:

            # Stop when all possible connections are made
            if len(self.already_visited) == len(self.total_connections):
                break

            # Create new traject
            traject = []
            traject_duration = 0

            city_id = random.randint(0, (len(self.locations) - 1))
            # Find the key (station) with the value (city id)
            station = list(self.locations.keys())[list(self.locations.values()).index(city_id)]
            traject.append(station)
            current_station = station

            # Keep adding stations to the traject until the time limit is reached
            while True:
                if traject_duration > self.time_limit:
                    break

                # Stop when all possible connections are made
                if len(self.already_visited) == len(self.total_connections):
                    break

                station2 = self.get_station()
                neighbours = self.get_neighbours(current_station)
                time = self.check_connection(neighbours, station2, current_station)

                if time is not None:
                    traject.append(station2)
                    connection = [current_station, station2]
                    self.already_visited.append(connection)

                    current_station = station2
                    # Add the time to get there to the traject and total duration
                    self.total_duration += time
                    traject_duration += time

            if len(traject) > 1:
                # Add the traject to the lijnvoering
                self.all_routes.append(traject)
                i += 1

        self.print_score()


    def get_station(self):
        # Generate random number for the new station city id
        city2_id = random.randint(0, (len(self.locations) - 1))
        # Find the key (station) with the value (city id)
        station2 = list(self.locations.keys())[list(self.locations.values()).index(city2_id)]
        return station2

    # Get the neighbours from a specific station
    def get_neighbours(self, current_station):
        possible_locations = []
        for city in self.total_connections:
            if city[0] == current_station:
                possible_locations.append(city)

            elif city[1] == current_station:
                possible_locations.append(city)

        return possible_locations

    # This check of the two stations are connected and returns the time to get there
    def check_connection(self, neighbours, station2, current_station):
        time = None
        for row in neighbours:
            if station2 in row and station2 != current_station:
                time = int(row[2])
        return time

    # Calculate and write the score in a CSV file
    def print_score(self):
        x = 1
        route = [["train", "station"]]
        for row in self.all_routes:
            route.append(["train_{}".format(x), row])
            x += 1

        p = len(self.already_visited) / len(self.total_connections)
        score = p * 10000 - (self.num_trajecten * 100 + self.total_duration)
        route.append(["score", score])
        file = open('outputjulia.csv', 'w')
        with file:
            writer = csv.writer(file)
            writer.writerows(route)

if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")
    all_locations = connections.get_locations()
    all_connections = connections.get_all_connections()
    start = Trainroutes(connections, all_locations, all_connections).add_trajects()