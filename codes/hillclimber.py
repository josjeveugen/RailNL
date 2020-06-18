import random

class Algorithm(object):
    def __init__(self, connections, trajects, used_connections):
        self.trajects = trajects
        self.all_connections = connections.connections
        self.cities = connections.cities
        self.used_connections = used_connections
        
        self.find_solution()
        
    
    def find_solution(self):
        #for i in range(100):
        self.delete_2_trajects()
        self.generate_2_new_trajects()
        self.check_score()
        
        
    def delete_2_trajects(self):
        for i in range(2):
            random_val = random.randint(0, len(self.trajects) - 1)
            del self.trajects[random_val]
        
        self.used_connections = self.check_used_connections()

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
    
    def generate_2_new_trajects(self):
        for i in range(2):
            start = random.randint(0, len(self.cities) - 1)
            start_city = self.cities[start]
            time = 0
            # wordt gebruikt om te checken of het traject niet over tijdslimiet gaat.
            under_timelimit = True
            traject = [start_city.name]
            
            while under_timelimit:
                # stopt het find_traject algoritme wanneer alle verbindingen al zijn gemaakt
                if len(self.used_connections) > len(self.all_connections):
                    return self.score(), self.trajects, self.used_connections
                
                # checkt welke neighbours er zijn en of ze niet dubbel gebruikt zullen worden.
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)
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
                if city_pair not in self.used_connections:
                    self.used_connections.append(city_pair)
                
                start_city = next_city

            self.trajects.append(traject)
            self.total_time += time