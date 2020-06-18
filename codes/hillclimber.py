import random

class Algorithm(object):
    def __init__(self, connections, trajects, used_connections):
        self.trajects = trajects
        self.all_connections = connections.connections
        self.used_connections = used_connections
        
        self.find_solution()
        
    
    def find_solution(self):
        print("1")
        print(self.trajects)
        print(self.used_connections)
        self.delete_2_trajects()
        
    def delete_2_trajects(self):
        for i in range(2):
            random_val = random.randint(0, len(self.trajects) - 1)
            del self.trajects[random_val]
        
        self.used_connections = self.check_used_connections()
        
        print("2")
        print(self.trajects)
        print(self.used_connections)
        
        
        
        
    def check_used_connections(self):
        new_used = []
        for traject in self.trajects:
            city1 = traject[0]
            for i in range(1, len(traject)):
                city2 = traject[i]
                city_pair = [city1, city2]
                city_pair.sort()
                if city_pair not in new_used:
                    new_used.append(city_pair)
                
                city1 = city2
                
        return new_used