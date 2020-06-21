import random
import csv
import matplotlib.pyplot as plt

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
        
        print(self.all_connections)
     
    # dit is het random algoritme dat de trajecten probeert te vinden.
    def find_traject(self):
        #starter_cities = self.less_neighbours()
        
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
                    return self.score(), self.trajects, self.used_connections, self.total_time
                    #return self.output()
    
                
                # checkt welke neighbours er zijn en of ze niet dubbel gebruikt zullen worden.
                neighbours = start_city.get_neighbours()
                neighbours = self.check_traject(start_city, neighbours)
                
                next_city = self.choose_shortest_time_forward(start_city)
                
                # voorkomt dat greedy onnodig dezelfde verbinding kiest
                if self.dubble_connection(traject, next_city):
                    # bij greedy kun je meteen breaken, omdat het anders steeds
                    # dezelfde keuze maakt.
                    break
                
                
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
            
        #return self.output()
        return self.score(), self.trajects, self.used_connections, self.total_time
    
    def dubble_connection(self, traject, city_name):
        if len(traject) > 1 and city_name == traject[-2]:
            return True
        return False
    
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
    
    def choose_shortest_time(self, city, neighbours):
        prev_neigh = neighbours[0]
        best_neigh = prev_neigh

        for neighbour in neighbours:
            if city.get_time(neighbour) < city.get_time(prev_neigh):
                best_neigh = neighbour

        return best_neigh
    
    def choose_shortest_time_forward(self, city):
        # random een pad uitkiezen, kijken welk pad het minst langst duurde
        # maar kijk ook wel pad het langste is.
        # of kijken naar het pad dat veel buren heeft?
        
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