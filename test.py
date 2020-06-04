import csv
# Loads the connections in a dictionary
class Connections(object):
    def __init__(self, connections_file):
        self.load_cities(connections_file)

    def load_cities(self, connections_file):

        cities = {}
        with open(connections_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                connections = []
                connections.append(row["station2"])
                connections.append(row["distance"])

                if row["station1"] in cities.keys():
                    current = row["station1"]
                    old = cities[current]
                    cities[row["station1"]] = old + connections

                else:
                    cities[row["station1"]] = connections

        print(f"All the connections: \n", cities)
        print("\n")
        print(f"Example --> all the connections from Zaandam: ", cities["Zaandam"])
        print("\n")

        if "Beverwijk" in cities["Zaandam"]:
            print("Check to see if Beverwijk is connected with Zaandam: It is")
        else:
            print("Check to see if Beverwijk is connected with Zaandam: It isn't")

if __name__ == "__main__":
    connections = [["adam", "eindhoven", 5], ["adam", "utrecht", 10], ["adam", "urk", 9]]
    test = Connections("data/ConnectiesHolland.csv")



