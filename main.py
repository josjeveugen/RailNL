from codes import connections
from codes import random_algoritme as r
from codes import test_hillclimber as hc
from codes import greedy as g

if __name__ == "__main__":
    # Run the connections class with the connections file
    load_connections = connections.Connections("data/ConnectiesHolland.csv")

    # Verwijder comment van het algoritme wat je wil runnen

    # --------------------------- Random reassignment --------------------------
    # random = r.Random(load_connections).find_traject()

    # --------------------------- Run Hill climber algoritme --------------------------
    # hill_climber = hc.Hillclimb(load_connections).find_traject()
    
    # --------------------------- Run Greedy algoritme --------------------------
    greedy = g.Greedy(load_connections).find_traject()
    