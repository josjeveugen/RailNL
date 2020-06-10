from codes import connections
from codes import random_algoritme
from codes import test_hillclimber

if __name__ == "__main__":
    # Run the connections class with the connections file
    load_connections = connections.Connections("data/ConnectiesHolland.csv")

    # Verwijder comment van het algoritme wat je wil runnen

    # --------------------------- Random reassignment --------------------------
    # random = random_algoritme.Random(load_connections).find_traject()

    # --------------------------- Run Hill climber algoritme --------------------------
    hill_climber = test_hillclimber.Hillclimb(load_connections).find_traject()