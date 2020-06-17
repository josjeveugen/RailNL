from codes import connections
from codes import random_algoritme as r
from codes import greedy as g
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Run the connections class with the connections file
    load_connections = connections.Connections("data/ConnectiesNationaal.csv")

    # Verwijder comment van het algoritme wat je wil runnen

    # --------------------------- Random reassignment --------------------------
    # random = r.Random(load_connections).find_traject()

    # --------------------------- Run Hill climber algoritme --------------------------
    # hill_climber = hc.Hillclimb(load_connections).find_traject()
    
    # --------------------------- Run Greedy algoritme --------------------------
    greedy = g.Greedy(load_connections)

    
def calculate_mean_score(x = 100):
    scores = []
    for i in range(x):
        #choose algorithm you want to run
        scores = g.Greedy(load_connections).find_traject()
    print(scores)
    print(max(scores), min(scores))
    plt.plot(scores)
    plt.show()
    # probleem is dat je terminal zal blijven runnen vanwege plt.show()
    # dus je moet je terminal beënidgen wanneer je iets nieuws wilt.

def calculate_average(max_loop = 100):
    scores = []
    sum = 0
    sum_connections = 0
    sum_trajects = 0
    total_time = 0
    for i in range(max_loop):
        score, con, trajects, time = hc.Hillclimb(load_connections).score()
        sum += score
        sum_connections += con
        sum_trajects += trajects
        total_time += time
        scores.append(score)

    average = sum / max_loop
    average_connections = sum_connections / max_loop
    average_trajects = sum_trajects / max_loop
    average_time = total_time / max_loop

    print("Average:", average)
    print("Average connections:", average_connections)
    print("Average trajects:", average_trajects)
    print("Average time:", average_time)

