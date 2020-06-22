from codes import connections
from codes import random_algoritme as r
from codes import dijkstra_algoritme as g
from codes import greedy_lookahead as gf
from codes import hillclimber as hc
import matplotlib.pyplot as plt
import csv
import numpy as np


# om dit te laten werken zijn een aantal veranderingen nodig...
# - class naam wordt: Algorithm
# - even kijken bij random_algorithm wat je moet veranderen in __init__
#   daar zie je args, dit heet nu zo, zodat dezelfde functie ook met
#   greedy lookahead werkt.
# - de output van een algoritme zijn 4 dingen: self.score(), self.trajects, self.used_connections,
#   self.total_time (de output wordt nu in deze file gemaakt, scheelt wat extra loops)
#   in de compare output functie zie je waarom, daar worden de scores vgl,
#   en wordt uiteindelijk de beste wordt gegenereerd.
#   belangrijk is self.used_connections terug te geven voor de hillclimber!
#   hetzelfde geldt ook voor self.total_time!
# - de final_traject om hem ready te maken voor de output moet er uit!
#   dit wordt gedaan in generate_output functie. Dit is nodig omdat hillclimber
#   anders niet werkt.
# That's it! Ga er vooral mee spelen en probeer fouten/verbeteringen te vinden :-)


# Puts the best output in a csv file.
def generate_output(score, trajects):
    output_trajects = []
    for traject in trajects:
        final_traject = "[%s]" % (', '.join(traject))
        output_trajects.append(final_traject)

    output = [["train", "stations"]]

    for i, traject in enumerate(output_trajects):
        string = "train_" + str(i)
        output.append([string, traject])
    output.append(["score", score])

    with open('results/output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(output)


# Compares generated outputs and returns the best.
def compare_outputs(algorithm, args):
    best_answer = algorithm.Algorithm(args).find_traject()
    for i in range(99):
        answer = algorithm.Algorithm(args).find_traject()
        if answer[0] > best_answer[0]:
            best_answer = answer
    return best_answer


# Asks and returns the output the user wants.
def prompt_algorithm():
    print("Welkom bij RailNL!\n")
    print("Welk spoorlijn probleem wil je oplossen?")
    print("  1: Holland")
    print("  2: Nationaal")
    
    while True:
        answer = input()
        if answer.isdigit():
            answer = int(answer)
        if answer == 1 or answer == 2:
            break
        print("Vul '1' of '2' in om een spoorlijn te kiezen")

    if answer == 1:
        max_time = 120
        max_trajects = 7
        load_connections = connections.Connections("data/ConnectiesHolland.csv")
    else:
        max_time = 180
        max_trajects = 20
        load_connections = connections.Connections("data/ConnectiesNationaal.csv")

    print("Met welk algoritme wil je dit oplossen?")
    print("  1: Random\n  2: Greedy\n  3: Greedy Lookahead")

    while True:
        answer = input()
        if answer.isdigit():
            answer = int(answer)
        if answer == 1 or answer == 2 or answer == 3:
            break
        print("Vul '1','2' of '3' in om een algoritme te kiezen")

    print("Wil je hillclimber toepassen op het gekozen algoritme?")
    print("  1: Ja\n  2: Nee")

    while True:
        hill_flag = input()
        if hill_flag.isdigit():
            hill_flag = int(hill_flag)
        if hill_flag == 1 or hill_flag == 2:
            break
        print("Vul '1' in om hillclimber toe te passen, vul anders '2'")
        
    if answer == 3:
        print("Hoeveel steden vooruit wil je in acht nemen (max = 20)?")
        steps = int(input())
        while answer not in range(1, 21):
            print("Kies een getal tussen 1 en 20...")
            steps = int(input())

    print("Top! We runnen het algoritme een paar keer zodat je hoogstwaarschijnlijk een goede uitkomst krijgt.\n")
    print("Dit kan even duren, een moment geduld alstublieft...")
    
    
    scores = []
    for i in range(1000):
        if answer == 1:
            algorithm = r
            best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects])
    
    
        elif answer == 2:
            algorithm = g
            best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects])
    
        elif answer == 3:
            algorithm = gf
            best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects, steps])
    
        if hill_flag == 1:
            # Run het hillclimber algoritme
            best_answer = hc.Algorithm(load_connections, best_answer[0], best_answer[1], best_answer[2], best_answer[3],
                                       max_time).find_solution()
        
        scores.append(best_answer[0])
    print(max(scores), min(scores), np.mean(scores))

    #generate_output(best_answer[0], best_answer[1])

    #print("Klaar! In de map 'results' is jouw uitkomst verschenen, deze zit in het bestand: 'output.csv'")
    plt.plot(scores)
    plt.show()


if __name__ == "__main__":
    prompt_algorithm()

    """
    # Run the connections class with the connections file
    load_connections = connections.Connections("data/ConnectiesNationaal.csv")
    # Verwijder comment van het algoritme wat je wil runnen
    # --------------------------- Random reassignment --------------------------
    # random = r.Random(load_connections).find_traject()
    # --------------------------- Run Hill climber algoritme --------------------------
    # hill_climber = hc.Hillclimb(load_connections).find_traject()

    # --------------------------- Run Greedy algoritme --------------------------
    #greedy = g.Algorithm(load_connections).find_traject()

    """
def calculate_mean_score(x=100):
    scores = []
    for i in range(x):
        # choose algorithm you want to run
        scores = g.Greedy(load_connections).find_traject()
    print(scores)
    print(max(scores), min(scores))
    plt.plot(scores)
    plt.show()
    # probleem is dat je terminal zal blijven runnen vanwege plt.show()
    # dus je moet je terminal beënidgen wanneer je iets nieuws wilt.


def calculate_average(max_loop=100):
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