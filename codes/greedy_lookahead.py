import random
import csv
import matplotlib.pyplot as plt

# Algorithm that checks ahead which neighbours will
# make a longer traject with a shorter duration
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
        self.steps = args[3]

    def find_traject(self):
        for i in range(self.max_trajects):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            # This is used to check whether the traject has exceeded the time limit
            under_timelimit = True
            traject = [start_city.name]

            while under_timelimit:
                # Stops the find traject algorithm when all connections are already made
                if len(self.used_connections) == len(self.all_connections):
                    return self.score(), self.trajects, self.used_connections, self.total_time

                # Checks the possible neighbours and if they have been used already
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)

                next_city = self.choose_shortest_time_forward(start_city)

                # Prevents greedy from choosing the same connection
                if self.dubble_connection(traject, next_city):
                    break

                next_time = start_city.get_time(next_city)

                # Start new traject if time limit has been exceeded
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                time += next_time
                traject.append(next_city.name)

                # Add new city to used_connections
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)

                start_city = next_city

            self.trajects.append(traject)
            self.total_time += time

        return self.score(), self.trajects, self.used_connections, self.total_time

    def dubble_connection(self, traject, city_name):
        if len(traject) > 1 and city_name == traject[-2]:
            return True
        return False

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

    def choose_shortest_time(self, city, neighbours):
        prev_neigh = neighbours[0]
        best_neigh = prev_neigh

        for neighbour in neighbours:
            if city.get_time(neighbour) < city.get_time(prev_neigh):
                best_neigh = neighbour

        return best_neigh

    def choose_shortest_time_forward(self, city):
        # Chooses a random path and checks which path has the shortest time
        trials = self.steps
        best_time = self.max_time
        best_traject = []
        best_neigh = None

        for trial in range(trials):
            first_city = self.choose_random_neighbour(city)
            traject = [first_city]
            time = 0
            start_city = first_city

            for step in range(1, self.steps):
                next_city = self.choose_random_neighbour(start_city)

                if self.dubble_connection(traject, next_city.name):
                    traject = traject[:-2]

                else:
                    time += start_city.get_time(next_city)
                    traject.append(next_city.name)

                start_city = next_city

                if len(traject) >= len(best_traject):
                    best_traject = traject
                    best_time = time
                    best_neigh = first_city

                elif len(traject) == len(best_traject) and time < best_time:
                    best_traject = traject
                    best_time = time
                    best_neigh = first_city

        return best_neigh

    def choose_random_neighbour(self, city):
        neighbours = city.get_neighbours()
        neighbours = self.check_traject(city, neighbours)
        return neighbours[random.randint(0, len(neighbours) - 1)]

    # Calculate score
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        return p * 10000 - (len(self.trajects) * 100 + self.total_time)
