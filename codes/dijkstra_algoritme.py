from operator import itemgetter
from connections import *
import random

class Random(object):

    def __init__(self, connections):
        self.ids = connections.city_ids
        self.connections = connections.connections
        self.trajects = []
        self.max_trajects = 7
        self.total_time = 0
        self.connections_added = []

    def check_connection(self):
        # Make time in self.connections an int instead of a string to be able to sort it later
        for connection in self.connections:
            connection[2] = int(connection[2])
            
        for i in range(self.max_trajects): 
            # Choose a random city to start with
            current_city = random.choice(list(self.ids.keys()))
            self.time = 0
            self.traject = [current_city]
            last_city = ""
            
            while True:
                possible_connections = []
                for connection in self.connections:
                    if current_city in connection:
                        possible_connections.append(connection)
                # Make sure going back to the station you came from is no option
                for connection in possible_connections:
                    if last_city in connection:
                        possible_connections.remove(connection)
                if not possible_connections:
                    break
                possible_connections.sort(key = lambda x: x[2])  
                back_up = []
                short_connection = possible_connections[0]
                for i in range(len(possible_connections)):
                    if possible_connections[i] not in self.connections_added:
                        short_connection = possible_connections[i]
                        break
                    elif all(con in possible_connections for con in self.connections_added):
                        short_connection = possible_connections[0]
                
                # If connection's not yet in the connections_added list, add
                if short_connection not in self.connections_added:
                    self.connections_added.append(short_connection)
                if self.time + int(short_connection[2]) > 120:
                    break
                self.time += int(short_connection[2])
                last_city = current_city
                if current_city == short_connection[1]:
                    current_city = short_connection[0]
                elif current_city in short_connection[0]:
                    current_city = short_connection[1]
                self.traject.append(current_city)
            self.trajects.append(self.traject)
            self.total_time += self.time
            if len(self.connections_added) == len(self.connections):
                break
            
        return self.output()
                 
    # Calculate the score
    def score(self):
        p = len(self.connections_added) / len(self.connections)
        t = len(self.trajects)
        Min = self.total_time
        quality = p * 10000 - (t * 100 + Min)
        return quality

    def output(self):
        score = self.score()
        i = 0
        for i in range(len(self.trajects)):
            print(("train_")+str(i) + str(self.trajects[i]))
        print(score)

if __name__ == "__main__":
    connections = Connections("data/ConnectiesHolland.csv")
    Random(connections).check_connection()
