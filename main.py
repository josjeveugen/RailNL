from codes import connections
from codes import random_algoritme as r
from codes import greedy_longest_path as glp
from codes import greedy_lookahead as gf
from codes import hillclimber as hc
import csv

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
    print("Welkom bij RailNL!\n\nWelk spoorlijn probleem wil je oplossen?")
    print("  1: Holland\n  2: Nationaal")
    
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
        
    if answer == 3:
        print("Hoeveel steden wil je vooruit kijken bij Greedy lookahead (max = 20)?")
        while True:
            steps = input()
            if steps.isdigit():
                steps = int(steps)
            if steps in range(1, 21):
                break
            print("Kies een getal tussen 1 en 20...")

    print("Op welke manier wil je de beginstad van ieder traject kiezen?")
    print("  1: Random\n  2: Meeste buren\n  3: Minste buren")
    

    print("Wil je hillclimber toepassen op het gekozen algoritme?")
    print("  1: Ja\n  2: Nee")

    while True:
        hill_flag = input()
        if hill_flag.isdigit():
            hill_flag = int(hill_flag)
        if hill_flag == 1 or hill_flag == 2:
            break
        print("Vul '1' in om hillclimber toe te passen, vul anders '2' in")
              
            
    print("Top! We runnen het algoritme een paar keer zodat je hoogstwaarschijnlijk een goede uitkomst krijgt.\n")
    print("Dit kan even duren, een moment geduld alstublieft...")
    
    if answer == 1:
        algorithm = r
        best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects])


    elif answer == 2:
        algorithm = glp
        best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects])

    elif answer == 3:
        algorithm = gf
        best_answer = compare_outputs(algorithm, [load_connections, max_time, max_trajects, steps])

    # Run hill climber algoritme
    if hill_flag == 1:
        best_answer = hc.Algorithm(load_connections, best_answer[0], best_answer[1], best_answer[2], best_answer[3],
                                   max_time).find_solution()


    generate_output(best_answer[0], best_answer[1])
    print(best_answer[0])
    print("Klaar! In de map 'results' is jouw uitkomst verschenen, deze zit in het bestand: 'output.csv'")


if __name__ == "__main__":
    prompt_algorithm()