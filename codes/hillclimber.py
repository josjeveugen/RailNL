import random

class Algorithm(object):
    def __init__(self, connections, score, trajects, used_connections, total_time, max_time):
        self.all_connections = connections.connections
        self.cities = connections.cities
        self.ids = connections.city_ids

        self.score = score
        self.trajects = trajects
        self.used_connections = used_connections
        self.total_time = total_time
        self.max_time = max_time

    def find_solution(self):
        for i in range(5):
            new_trajects, new_used, new_time = self.delete_2_trajects()
            new_trajects, new_used, new_score = self.generate_2_new_trajects(new_trajects, new_used, new_time)

            print(new_score, self.score)
            if new_score > self.score:
                self.trajects = new_trajects
                self.used_connections = new_used
                self.total_time = new_time
                self.score = new_score
            print(self.trajects)

        return self.score, self.trajects

    def delete_2_trajects(self):
        new_trajects = self.trajects.copy()
        for i in range(2):
            random_val = random.randint(0, len(new_trajects) - 1)
            del new_trajects[random_val]

        return self.adjust_new_con_and_time(new_trajects)

    def adjust_new_con_and_time(self, new_trajects):
        new_used = []
        new_time = 0
        for traject in new_trajects:
            city1 = traject[0]
            for i in range(1, len(traject)):
                city2 = traject[i]
                # adding the connection to new used connection
                city_pair = [city1, city2]
                city_pair.sort()
                if city_pair not in new_used:
                    new_used.append(city_pair)

                # adding the time to new total time
                city1_node = self.cities[self.ids[city1]]
                city2_node = self.cities[self.ids[city2]]
                new_time += city1_node.get_time(city2_node)

                city1 = city2

        return new_trajects, new_used, new_time

    def generate_2_new_trajects(self, new_trajects, new_used, new_time):
        for i in range(2):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            # wordt gebruikt om te checken of het traject niet over tijdslimiet gaat.
            under_timelimit = True
            traject = [start_city.name]

            while under_timelimit:
                # stopt het find_traject algoritme wanneer alle verbindingen al zijn gemaakt
                if len(new_used) == len(self.all_connections):
                    return new_trajects, new_used, self.new_score(new_trajects, new_used, new_time)

                # checkt welke neighbours er zijn en of ze niet dubbel gebruikt zullen worden.
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours, new_used)
                # random buur kiezen
                random_val = random.randint(0, len(neighbours) - 1)
                next_city = neighbours[random_val]
                next_time = start_city.get_time(next_city)

                # begint nieuw traject als het tijdslimiet overschreden is.
                if time + next_time >= self.max_time:
                    under_timelimit = False
                    break

                traject.append(next_city.name)
                time += next_time

                # nieuwe stad wordt toegevoegd aan used_connections
                city_pair = [start_city.name, next_city.name]
                city_pair.sort()
                if city_pair not in new_used:
                    new_used.append(city_pair)

                start_city = next_city

            new_trajects.append(traject)
            new_time += time

        return new_trajects, new_used, self.new_score(new_trajects, new_used, new_time)

    def check_traject(self, city, neighbours, new_used):
        new_neigh = []
        for neighbour in neighbours:
            city_pair = [city.name, neighbour.name]
            city_pair.sort()
            if city_pair not in new_used:
                new_neigh.append(neighbour)

        # geeft de alle buren mee indien alle buren als eens zijn gebruikt.
        if new_neigh == []:
            return neighbours
        return new_neigh

    def new_score(self, new_trajects, new_used, new_time):
        p = len(new_used) / len(self.all_connections)
        return p * 10000 - (len(new_trajects) * 100 + new_time)