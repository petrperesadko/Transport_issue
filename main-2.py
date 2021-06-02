from datetime import datetime


class Route:

    def __init__(self, list_x):
        self.stations = dict()
        for n in range(4, len(list_x), 2):
            self.stations[list_x[n]] = list_x[n+1]
        self.name = list_x[0]
        temporary = list_x[1].split(':')
        self.first_bus = int(temporary[0]) * 60 + int(temporary[1])
        temporary = list_x[2].split(':')
        self.last_bus = int(temporary[0]) * 60 + int(temporary[1])
        if self.last_bus < self.first_bus:
            self.last_bus += 1440
        self.time_gap = int(list_x[3])

    def print(self):
        print(self.stations)


all_routes = []
amount_of_routes = 0
classes = []
file = open('timetable.txt', 'r')
for single_line in file:
    temporary_list = [elt.strip() for elt in single_line.split(';')]
    # all_routes.append(temporary_list)
    new_route = Route(temporary_list)
    classes.append(new_route)
    amount_of_routes += 1
file.close()


def is_there_such_station(route, n):
    is_true = False
    counter = 0
    for time, name in route.stations.items():
        if name == n:
            is_true = True
        if not is_true:
            counter += 1
    return is_true, counter


def get_time_to_station(route, n):
    found = False
    if is_there_such_station(route, n)[0]:
        found = True
        counter = is_there_such_station(route, n)[1]
        list_from_dict = list(route.stations.items())
        time = datetime.now()
        time_now = time.hour * 60 + time.minute
        if time_now < route.first_bus:
            time_now += 1440
        # for iterator, val1 in enumerate(list_from_dict):
        #     print("list", list_from_dict[iterator][0])
        #     print("iter0", iterator)
        #     print("val0", val1[0])
        #     print("val1", val1[1])
        boolean = False
        if counter == 0 and not boolean:
            time_of_closest = route.first_bus
            while time_of_closest <= time_now:
                time_of_closest += route.time_gap
            if time_of_closest - time_now <= 10 and time_now <= route.last_bus:
                # print(time_of_closest - time_now)
                answers[route.name, list_from_dict[1][1]] = time_of_closest - time_now
                # return route.stations[0], time_of_closest - time_now
            boolean = True
        if counter == len(list_from_dict) - 1 and not boolean:
            time_of_closest = route.first_bus
            while time_of_closest <= time_now:
                time_of_closest += route.time_gap
            if time_of_closest - time_now <= 10 and time_now <= route.last_bus:
                # print(time_of_closest - time_now)
                answers[route.name, list_from_dict[len(list_from_dict) - 2][1]] = time_of_closest - time_now
                # return route.stations[len(list_from_dict) - 1], time_of_closest - time_now
            boolean = True
        elif not boolean:
            time_next = 0
            time_prev = 0
            for iterator in enumerate(list_from_dict):
                time_next += int(list_from_dict[iterator[0]][0])
                if int(iterator[0]) == counter:
                    # print(time_next)
                    break
            for iterator, value in enumerate(list_from_dict):
                if int(len(list_from_dict) - 1 - int(iterator)) == counter:
                    # print(time_prev)
                    break
                time_prev += int(list_from_dict[len(list_from_dict) - 1 - int(iterator)][0])
            time_next += route.first_bus
            time_prev += route.first_bus
            while time_next <= time_now:
                time_next += route.time_gap
            while time_prev <= time_now:
                time_prev += route.time_gap
            if time_next - time_now <= 10 and time_now <= route.last_bus:
                # print(time_next - time_now)
                answers[route.name, list_from_dict[counter + 1][1]] = time_next - time_now
            if time_prev - time_now <= 10 and time_now <= route.last_bus:
                # print(time_prev - time_now)
                answers[route.name, list_from_dict[counter - 1][1]] = time_prev - time_now
            boolean = True
    return found

running = True
while running:
    station_name = input("Enter station: ")
    if not station_name:
        running = False
    answers = dict()
    works = False
    for single_class in classes:
        if get_time_to_station(single_class, station_name):
            works = True
        else:
            works = False
            # print(single_class.name, ",", )
    sorted_tuple = sorted(answers.items(), key=lambda x: x[1])
    if works:
        for words in sorted_tuple:
            print(words)

    # A = Route(0)
    # A.assign()
    # A.print()
    # station_name = "B"
    # if is_there_such_station(A, station_name)[0]:
    #     print("YES")
    #     print(get_time_to_station(A, station_name))
    # else:
    #     print("No such station found")
    # get_time_to_station(A, station_name)
