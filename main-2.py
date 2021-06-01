from datetime import datetime

all_routes = []
amount_of_routes = 0

file = open('timetable.txt','r')
for single_line in file:
    temporary_list = [elt.strip() for elt in single_line.split(';')]
    amount_of_routes += 1
    all_routes.append(temporary_list)
file.close()
print(all_routes)


class Route:

    def __init__(self, number):
        self.stations = {}
        for n in range(4, len(all_routes[number]) - 2, 1):
            self.stations[all_routes[number][n+1]] = all_routes[number][n]
        self.name = ""
        self.first_bus = 0
        self.last_bus = 0
        self.time_gap = 0

    def assign(self):
        for n in range(4, len(all_routes) - 2):
            self.stations[all_routes[0][n+1]] = all_routes[0][n]

    def print(self):
        print(self.stations)

running = True
while running:
    station_name = input("Enter station: ")
    if not station_name:
        running = False
    A = Route(0)
    # A.assign()
    A.print()



