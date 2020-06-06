import random
from connections import *

# Function that prints a random 'lijnvoering'
# It does not take already visited stations into account yet

def random_outcome(connections, locations, neighbours):
    # Determine how many trajects this lijnvoering will have by generating a random number
    # Min 1 Max 7
    num_trajecten = random.randint(1, 7)

    # Keeps track of the duration of the whole lijnvoering
    total_duration = 0

    # List that will contain all the trajecten and list containing already visited accounts
    all_routes = []
    already_visited = []

    # Create a traject until the number of trajecten is reached
    for i in range(0, num_trajecten):

        # Create empty traject list upon entering a new loop
        traject = []

        # While loop that generates a random number to look up a station with
        # Stops when a station is found that hasn't been visited yet
        # That station becomes the current station
        while True:
            # 22 stations so a number between 0 and 22
            city_id = random.randint(0, 21)

            # Find the key (station) with the value (city id)
            station = list(locations.keys())[list(locations.values()).index(city_id)]

            if station not in already_visited:
                break

        current_station = station

        # Add the station to the traject and list of already visited stations
        already_visited.append(station)
        traject.append(station)

        # Keep track of the duration of this particular traject
        traject_duration = 0

        # While loop that generates a random number to look up a station with
        # Will keep looping until a new station is found that is connected with the current station
        while True:
            if len(traject) == 4 or traject_duration > 119:
                break

            city2_id = random.randint(0, 21)
            station2 = list(locations.keys())[list(locations.values()).index(city2_id)]

            # Get the possible directions from current station
            neighbours = connections.get_neighbours(current_station)

            # Loop through the neighbours and if the found station is indeed connected with the
            # current station, add the station to the traject and make it the new current station
            for row in neighbours:
                if station2 in row and station2 != current_station:
                    traject.append(station2)
                    already_visited.append(station2)
                    current_station = station2

                    # Add the time to get there to the traject and total duration
                    time = int(row[2])
                    traject_duration += time
                    total_duration += time

        # End the traject to the lijnvoering
        all_routes.append(traject)


    x = 1
    for row in all_routes:
        print("train_{}:".format(x), row)
        x += 1

    if len(already_visited) == 21:
        fraction = 1
    else:
        fraction = 1

    score = fraction * 10000 - (num_trajecten *100 + total_duration)
    print("score: {}".format(score))






