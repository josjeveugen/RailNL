from connections import *
import random

# find a city to start your traject at random
class Random(object):
    
        
    def __init__(self, connections):
        self.ids = connections.city_ids
        self.connections = connections.connections
        self.trajects = []
        self.connections_added = []
        

        
    def check_connection(self):
        while len(self.trajects) < 7:
            # Generate first city at random
            self.current_city = random.choice(list(self.ids.keys()))
            self.time = 0
            self.traject = []
            while True:
                self.possible_connections = []
                # Check in all connection which cities are connected to current_city; add them to possible_connections
                for connection in self.connections:
                    # print(connection)
                    if self.current_city in connection:
                        if connection not in self.connections_added: 
                            self.possible_connections.append(connection)
                if len(self.possible_connections) == 0:
                    break               
                # Choose one random_connection out of possible_connections, and add if not used yet
                self.random_connection = random.choice(list(self.possible_connections))
                self.connections_added.append(self.random_connection)  
                    
                    # Keep track of duration of connection
                self.time += int(self.random_connection[2])
  
                # Change current_city to connected city, to make it the new current_city
                if self.current_city == self.random_connection[1]:
                    self.current_city = self.random_connection[0]
                elif self.current_city == self.random_connection[0]:
                    self.current_ciy = self.random_connection[1]
                self.traject.append(self.random_connection)    
                         
                if self.time > 121: 
                    break
                if self.traject not in self.trajects:    
                    self.trajects.append(self.traject)    
        return self.output()
            
        
    def output(self):
        i = 0  
        for traject in self.trajects:
            output = "train_"+str(i) + str(traject)
            i += 1
            print(output)

       
if __name__ == "__main__":
    connections = Connections("data/ConnectiesHolland.csv")
    Random(connections).check_connection()


