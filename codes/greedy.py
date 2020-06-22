from .connections import City
from .connections import Connections
import random
import csv
import copy

# kopie van random.py file om algoritme van hill climber te testen

# idee is dat het random algoritme steeds random een buurstad kiest.
# het algoritme stopt wanneer het alle verbindingen heeft gehad.

class Greedy(object):
    def __init__(self, connections_object):
        all_cities = connections_object.cities
        self.cities = copy.deepcopy(all_cities)
        self.ids = connections_object.city_ids
        self.all_connections = connections_object.connections
        self.used_connections = []
        self.used_cities = []
        self.trajects = []
        self.max_trajects = 20
        self.max_time = 180
        self.total_time = 0
        self.find_traject()

    # dit is het random algoritme dat de trajecten probeert te vinden.
    def find_traject(self):
        for i in range(self.max_trajects):
            start_city = self.get_start()


            testn = start_city.get_neighbours()

            # wordt gebruikt om te checken of het traject niet over tijdslimiet gaat.
            under_timelimit = True

            traject = [start_city.name]
            doubles = 0
            time = 0

            while under_timelimit:
                # stopt het find_traject algoritme wanneer alle verbindingen al zijn gemaakt
                if len(self.used_connections) > len(self.all_connections):
                    return self.output()

                # checkt welke neighbours er zijn en of ze niet dubbel gebruikt zullen worden.
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours, doubles)

                if neighbours is None:
                    under_timelimit = False
                    break


                next_city = self.get_city(start_city, neighbours, traject)
                next_time = start_city.get_time(next_city)

                # begint nieuw traject als het tijdslimiet overschreden is.
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                # nieuwe stad wordt toegevoegd aan used_connections
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)
                else:
                    doubles += 1

                traject.append(next_city.name)
                time += next_time
                start_city = next_city


            # Remove the quotes from the traject list
            final_traject = "[%s]" % (', '.join(traject))
            self.trajects.append(final_traject)
            self.total_time += time

        # reset alles als de lijnvoering niet alle verbindingen heeft gemaakt
        return self.output()

    # Kiest een begin stad met klein aantal buren
    def get_start(self):
        possible_cities = []
        for x in self.cities:
            n = x.get_neighbours()
            if len(n) == 1:
                possible_cities.append(x)

        choose = []
        for p in possible_cities:
            if p not in self.used_cities:
                choose.append(p)

        if choose == []:
            start = random.randint(0, len(self.cities) - 1)
            city = self.cities[start]
            return city
        else:
            peep = random.randint(0, (len(choose) - 1))
            city = choose[peep]
            self.used_cities.append(city)
            self.cities.remove(city)
            return city




    # Kiest de stad die het dichts bij ligt door alle mogelijke buren te checken
    def get_city(self, city, neighbours, traject):
        # Greedy
        # Kies random state
        random_val = random.randint(0, len(neighbours) - 1)
        next_city = neighbours[random_val]
        check_neighs = next_city.get_neighbours()
        best_percentage = self.used_options(next_city.name)
        best_count = len(check_neighs)


        # Doe beste van alle mogelijke verbindingen
        for neighbour in neighbours:
            check_neighs = neighbour.get_neighbours()
            neigh_count = len(check_neighs)
            city_pair = [city.name, neighbour.name]
            city_pair.sort()

            # Check of die verbinding al is gemaakt
            if city_pair not in self.used_connections:

                percentage_used = self.used_options(neighbour.name)
                # Verander de stad en tijd als de verbinding voordeliger is
                if neigh_count > best_count or percentage_used < best_percentage:
                    next_city = neighbour
                    best_count = neigh_count
                    best_percentage = percentage_used

        return next_city

    def used_options(self, city):

        used_connections = []
        for x in self.used_connections:
            if city in x:
                used_connections.append(x)

        all_possibilities = []
        for y in self.all_connections:
            if city in y:
                all_possibilities.append(y)

        percentage_used = len(used_connections) / len(all_possibilities)

        return percentage_used

    # checkt of de buren niet al eerder zijn gebruikt.
    def check_traject(self, city, neighbours, doubles):
        new_neigh = []
        for neighbour in neighbours:
            city_pair = [city.name, neighbour.name]
            city_pair.sort()
            if city_pair not in self.used_connections:
                new_neigh.append(neighbour)

        if new_neigh == [] and doubles < 2:
            return neighbours
        if new_neigh == []:
            return None

        return new_neigh

    # berekent de kwaliteit van de lijnvoering
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        return (p * 10000 - (len(self.trajects) * 100 + self.total_time))