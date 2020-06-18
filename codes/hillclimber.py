import random

class Algorithm(object):
    def __init__(self, connections, trajects):
        self.trajects = trajects
        self.all_connections = connections.connections
        self.used_connections = self.check_used_connections()
        
        print("ffff", self.used_connections)
        
        self.find_solution()
        
    def check_used_connections(self):
        print(self.all_connections)
        traject_con = []
        for traject in self.trajects:
            traject_con.append(traject)
        
        used = []
        
        print("xx", traject_con)
            
        for connection in self.all_connections:
            if connection[:-1] in traject_con:
                used.append(connection[:-1])
        
        return used
        
    
    def find_solution(self):
        print(self.trajects)
        #self.delete_2_trajects()
        
    def delete_2_trajects(self):
        random_val = random.randint(0, len(neighbours) - 1)
        