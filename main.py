from codes import connections
from codes import random_algoritme as r
from codes import greedy as g
from codes import greedy_lookahead as gf
from codes import hillclimber as hc
import matplotlib.pyplot as plt
import csv


# om dit te laten werken zijn een aantal veranderingen nodig...
# - class naam wordt: Algorithm
# - even kijken bij random_algorithm wat je moet veranderen in __init__
#   daar zie je args, dit heet nu zo, zodat dezelfde functie ook met
#   greedy lookahead werkt.
# - de output moet worden: self.score(), self.trajects, self.used_connections (de output wordt nu
#   in deze file gemaakt, scheelt wat extra loops)
#   in de compare output functie zie je waarom, daar worden de scores vgl,
#   en wordt uiteindelijk de beste wordt gegenereerd.
#   belangrijk is self.used_connections terug te geven voor de hillclimber!
# That's it! Ga er vooral mee spelen en probeer fouten/verbeteringen te vinden :-)


# Puts the best output in a csv file.
def generate_output(score, trajects):
    output = [["train", "stations"]]

    for i, traject in enumerate(trajects):
        string = "train_"+str(i)
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
    print("  1: Noord-Holland")
    print("  2: Nationaal")
    
    answer = int(input())
    while answer != 1 and answer != 2:
        print("Je moet een getal van 1 of 2 invullen...")
        answer = int(input())
    
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
    
    answer = int(input())
    while answer != 1 and answer != 2 and answer != 3:
        print("Je moet een getal van 1, 2 of 3 invullen...")
        answer = int(input())
        
    print("Wil je hillclimber toepassen op het gekozen algoritme?")
    print("  0: Nee\n  1: Ja")
    
    hill_flag = int(input())
    while hill_flag != 0 and hill_flag != 1:
        print("Je moet een getal van 0 of 1 invullen...")
        hill_flag = int(input())
    
    print("Top! We runnen het algoritme een paar keer zodat je hoogstwaarschijnlijk een goede uitkomst krijgt.\n")
    print("Dit kan even duren, een moment geduld alstublieft...")
    
    if answer == 1:
        algorithm = r
        best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects])
        
    elif answer == 2:
        # nog even beslissen hoe en wat met greedy
        print("Not done yet...")
        
    elif answer == 3:
        algorithm = gf
        print("Hoeveel steden vooruit wil je in acht nemen (max = 20)?")
        steps = int(input())
        while answer not in range(1, 21):
            print("Kies een getal tussen 1 en 20...")
            steps = int(input())
        
        best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects, steps])
    
    if hill_flag:
        # Run het hillclimber algoritme
        best_answer = hc.Algorithm(load_connections, best_answer[1])
        return 0
    
    generate_output(best_answer[0], best_answer[1])
        
    print("Klaar! In de map 'data' is jouw uitkomst verschenen, deze zit in het bestand: 'output.csv'")

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
    greedy = g.Greedy(load_connections)
    """

    
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

