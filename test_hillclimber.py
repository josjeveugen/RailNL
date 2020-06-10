from connections import City
from connections import Connections
import random
import csv

# kopie van random.py file om algoritme van hill climber te testen

# idee is dat het random algoritme steeds random een buurstad kiest.
# het algoritme stopt wanneer het alle verbindingen heeft gehad.

class Random(object):
    def __init__(self, connections_object):
        self.cities = connections_object.cities
        self.ids = connections_object.city_ids
        self.all_connections = connections_object.connections
        self.used_connections = []
        self.trajects = []
        self.max_trajects = 7
        self.max_time = 120
        self.total_time = 0


    # dit is het random algoritme dat de trajecten probeert te vinden.
    def find_traject(self):
        for i in range(self.max_trajects):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            # wordt gebruikt om te checken of het traject niet over tijdslimiet gaat.
            under_timelimit = True
            traject = [start_city.name]


            while under_timelimit:
                # stopt het find_traject algoritme wanneer alle verbindingen al zijn gemaakt
                if len(self.used_connections) == len(self.all_connections):
                    return self.output()

                # checkt welke neighbours er zijn en of ze niet dubbel gebruikt zullen worden.
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)
                
                # kies een buur aan de hand van welke verbinding het kortst is
                next_city = self.get_city(start_city, neighbours)
                traject.append(next_city.name)
                next_time = start_city.get_time(next_city)

                # begint nieuw traject als het tijdslimiet overschreden is.
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                time += next_time

                # nieuwe stad wordt toegevoegd aan used_connections
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)

                start_city = next_city

            self.trajects.append(traject)
            self.total_time += time

        return self.output()

    # Kiest de stad die het dichts bij ligt door alle mogelijke buren te checken
    def get_city(self, city, neighbours):
        # Hill climber
        # Kies random state
        random_val = random.randint(0, len(neighbours) - 1)
        next_city = neighbours[random_val]
        time = city.get_time(next_city)

        print("huidige city:", city.name)
        print("huidige next city:", next_city.name)
        print("huidige time:", time)

        # Doe beste van alle mogelijke verbindingen
        for neighbour in neighbours:
            print("Neighbour:", neighbour.name)
            check_city = neighbour.name
            check_time = city.get_time(neighbour)
            print("Neighbour time:", check_time)


            # Check of die verbinding al is gemaakt
            city_pair = [city.name, check_city]
            city_pair.sort()

            if city_pair not in self.used_connections:
                # Verander de stad en tijd als de verbinding voordeliger is
                if check_time < time:
                    next_city = neighbour
                    time = check_time

            print("New time:", time)

        print("huidige city:", city.name)
        print("final next city:", next_city.name)
        print("final time:", time)
        print("\n")
        return next_city

    # checkt of de buren niet al eerder zijn gebruikt.
    def check_traject(self, city, neighbours):
        new_neigh = []

        for neighbour in neighbours:
            city_pair = [city.name, neighbour.name]
            city_pair.sort()
            if city_pair not in self.used_connections:
                new_neigh.append(neighbour)

        # geeft de alle buren mee indien alle buren als eens zijn gebruikt.
        if new_neigh == []:
            return neighbours
        return new_neigh

    # berekent de kwaliteit van de lijnvoering
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        print(len(self.used_connections), len(self.all_connections))

        return p * 10000 - (len(self.trajects) * 100 + self.total_time)

    # geeft de output voor in het csv bestand.
    def output(self):
        score = self.score()
        output = [["train", "stations"]]
        for i, traject in enumerate(self.trajects):
            string = "train_" + str(i)
            output.append([string, traject])
            print(["train_{}".format(i), traject])
        output.append(["score", score])
        print("score", score)

        with open('output_julia.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(output)
        pass


if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")
    test = Random(connections).find_traject()

