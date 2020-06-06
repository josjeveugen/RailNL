import random
from connections import *

# Function that prints a random 'lijnvoering'
# It does not take already used connections into account yet

def random_outcome(connections, locations, neighbours):
    # Determine how many trajects this lijnvoering will have by generating a random number
    # Min 1 Max 7
    num_trajecten = random.randint(1, 7)
    all_connections = neighbours

    # Keeps track of the duration of the whole lijnvoering
    total_duration = 0

    # List that will contain all the trajecten and list containing already visited accounts
    all_routes = []
    already_visited = []

    # Create a traject until the number of trajecten is reached
    for i in range(0, num_trajecten):

        # Create empty traject list upon entering a new loop
        traject = []

        # 22 stations so a number between 0 and 22
        city_id = random.randint(0, 21)

        # Find the key (station) with the value (city id)
        station = list(locations.keys())[list(locations.values()).index(city_id)]

        # That station becomes the current station
        current_station = station

        # Add the station to the traject
        traject.append(station)

        # Keep track of the duration of this particular traject
        traject_duration = 0

        # While loop that generates a random number to look up a station with
        # Will keep looping until a new station is found that is connected with the current station
        while True:

            # Stops the loop and moves on to the next traject when the 2 hour limit is reached
            if traject_duration > 119:
                break

            # Generate random number for the new station city id
            city2_id = random.randint(0, 21)

            # Find the key (station) with the value (city id)
            station2 = list(locations.keys())[list(locations.values()).index(city2_id)]

            # Get the possible directions from current station
            neighbours = connections.get_neighbours(current_station)

            # Loop through the neighbours and if the new station is indeed connected with the
            # current station, add the station to the traject and make it the new current station
            for row in neighbours:
                if station2 in row and station2 != current_station:
                    traject.append(station2)
                    connection = [current_station, station2]
                    already_visited.append(connection)
                    current_station = station2

                    # Add the time to get there to the traject and total duration
                    time = int(row[2])
                    traject_duration += time
                    total_duration += time

        # End the traject to the lijnvoering
        all_routes.append(traject)

    # Loop through all the trajects in the lijnvoering and print them
    x = 1
    for row in all_routes:
        print("train_{}:".format(x), row)
        x += 1

    p = len(already_visited) / len(all_connections)
    # Calculate score and print it
    score = p * 10000 - (num_trajecten * 100 + total_duration)
    print("score: {}".format(score))


if __name__ == "__main__":
    # Run the connections class with the connections file
    connections = Connections("data/ConnectiesHolland.csv")

    all_locations = connections.get_locations()
    all_connections = connections.get_all_connections()
    random_outcome(connections, all_locations, all_connections)




