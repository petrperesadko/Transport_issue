from datetime import datetime


def find_station_name(some_route, some_name):
    route = list()
    for i in range(4, len(some_route), 2):
        route.append(some_route[i])
    if some_name in route:
        return True
    else:
        return False

def calculate_time(some_list, some_name):
    route_name = some_list[0]
    s = some_list[1]
    s = s.split(':')
    begin_time = int(s[0]) * 60 + int(s[1])
    s = some_list[2]
    s = s.split(':')
    end_time = int(s[0]) * 60 + int(s[1])
    interval_time = int(some_list[3])
    some_route = list()
    some_route_time = list()
    some_route_time.append(0)
    for i in range(4, len(some_list), 2):
        some_route.append(some_list[i])
    for i in range(5, len(some_list), 2):
        some_route_time.append(int(some_list[i]))
    flag = False
    some_time = datetime.now()
    current_time = some_time.hour * 60 + some_time.minute
    time_forward = 0
    time_backwards = 0
    if some_route[0] == some_name:
        flag = True
        temp = begin_time
        while temp <= current_time:
            temp += interval_time
        # print("Current time: ", time_to_display)
        # print(f'{station_name},', "destination", f'{some_route[1]},', temp - current_time, "min")
        dictionary[route_name, some_route[1]] = temp - current_time
    if some_route[len(some_route) - 1] == some_name and not flag:
        flag = True
        temp = begin_time
        while temp <= current_time:
            temp += interval_time
        # print("Current time: ", time_to_display)
        # print(f'{station_name},', "destination", some_route[len(some_route) - 2], ",",
        #       temp - current_time, "min")
        dictionary[route_name, some_route[len(some_route) - 2]] = temp - current_time
    elif not flag:
        # current_time = some_time.hour * 60 + some_time.minute
        # time_forward = 0
        # time_backwards = 0
        station_number = 0
        for counter, item in enumerate(some_route):
            time_forward += some_route_time[counter]
            station_number = counter
            if item == some_name:
                break
        # for counter, item in enumerate(some_route):
        #     time_forward += some_route_time[counter]
        #     time_backwards += some_route_time[len(some_route) - 1 - counter]
        #     if item == some_name:
        #         break
        for counter, item in enumerate(some_route):
            time_backwards += some_route_time[len(some_route) - 1 - counter]
            if item == some_name:
                break

        first_stop_time_forward = begin_time + time_forward
        first_stop_time_backwards = begin_time + time_backwards

        while first_stop_time_forward <= current_time:
            first_stop_time_forward += interval_time
        while first_stop_time_backwards <= current_time:
            first_stop_time_backwards += interval_time

        # print("Current time: ", time_to_display)
        # print(f'{station_name},', "destination", f'{some_route[station_number + 1]},',
        #       first_stop_time_forward - current_time)
        # print(f'{station_name},', "destination", f'{some_route[station_number - 1]},',
        #       first_stop_time_backwards - current_time)
        dictionary[route_name, some_route[station_number + 1]] = first_stop_time_forward - current_time
        dictionary[route_name, some_route[station_number - 1]] = first_stop_time_backwards - current_time


list_of_routes = []
number_of_routes = 0
with open('data.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_routes.append(inner_list)
        number_of_routes += 1

while True:
    answer = input("Enter station: ")
    dictionary = dict()
    checked = False
    if not answer:
        break
    for i in range(number_of_routes):
        if find_station_name(list_of_routes[i], answer):
            checked = True
            calculate_time(list_of_routes[i], answer)
    if checked:
        time_to_display = datetime.now().strftime("%H:%M")
        print("Current time: ", time_to_display)
        for w in sorted(dictionary, key=dictionary.get, reverse=True):
            print("destination", f'{w},', dictionary[w], "min")
        # print(f'{station_name},', "destination", some_route[len(some_route) - 2], ",",
        #       temp - current_time, "min")

    if not checked:
        print("No such station!")