from operator import itemgetter
import random

# Algorithm that makes traject based on the closest neighbours
class Algorithm(object):
    def __init__(self, args):
        self.ids = args[0].city_ids
        self.cities = args[0].cities
        self.all_connections = args[0].connections        
        self.used_connections = []
        self.trajects = []        
        self.max_time = args[1]
        self.max_trajects = args[2]
        self.start = args[3]        
        self.total_time = 0

    def find_traject(self):
        cities = {}        
        if self.start != "random":
            for city in self.ids:
                connections = []
                for connection in self.all_connections:
                    if city in connection:
                        connections.append(connection)
                cities[city] = connections
            if self.start == "most":
                cities = sorted(cities.items(), key= lambda x: len(x[1]), reverse=True)
            if self.start == "least":
                cities = sorted(cities.items(), key= lambda x: len(x[1]))     
        for i in range(self.max_trajects):
            if self.start == "random":
                current_city = random.choice(list(self.ids.keys()))
            else:
                neighbours = []
                j = 0
                # Add the cities who have most neighbours to the list 'most'
                for j in range(len(cities)):
                    if len(cities[0][1]) == 1:  
                        for j in range(len(cities)):
                            neighbours.append(cities[j][0])
                    elif len(cities[j][1]) == len(cities[0][1]):
                        neighbours.append(cities[j][0])
                    j += 1
                # Get a random city from the list with cities with the most neighbours
                current_city = random.choice(neighbours)
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
                    elif i == len(possible_connections):
                        short_connection = possible_connections[0]
                if self.time + int(short_connection[2]) > self.max_time:
                    break
                # If connection's not yet in the connections_added list, add
                if short_connection not in self.used_connections:
                    self.used_connections.append(short_connection)
                # Delete a connection from the cities list, so it won't be used as starting city anymore
                for city in cities:
                    for connection in city[1]:
                        if connection == short_connection:
                            city[1].remove(short_connection)
                    if not city[1]:
                        cities.remove(city)
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
                break
        return self.score(), self.trajects, self.used_connections, self.total_time

    # Calculate the score
    def score(self):
        p = len(self.used_connections) / len(self.all_connections)
        quality = p * 10000 - (len(self.trajects) * 100 + self.total_time)
        return quality

    def output(self):
        score = self.score()
        output = [["train", "stations"]]
        for i in range(len(self.trajects)):
            print(("train_") + str(i) + str(self.trajects[i]))
        output.append(["score", score])
        print(score)

        with open('results/output_test.csv', 'w', newline='') as file:
            output_test = csv.writer(file, delimiter=',')
            output_test.writerows(output)
        pass
