from datetime import datetime


def find_station_name(some_route, some_name):
    if some_name in some_route:
        return True


def calculate_time(some_route, some_route_time, some_name, some_time, begin_time, end_time, interval_time):
    flag = False
    time_to_display = datetime.now().strftime("%H:%M")

    if some_route[0] == some_name:
        # new_time = some_time.replace(hour=some_time.hour, minute=some_time.minute + int(some_route_time[1]))
        print("Current time: ", time_to_display)
        print("destination", some_route[0], ",", some_route_time[1], "min")
        flag = True
    elif some_route[len(some_route) - 1] == some_name:
        print("Current time: ", time_to_display)
        print("destination", some_route[len(some_route) - 1], ",", some_route_time[len(some_route_time) - 1], "min")
        flag = True
    else:
        flag = True
        current_time = some_time.hour * 60 + some_time.minute
        time_forward = 0
        time_backwards = 0
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

        print("Current time: ", time_to_display)
        print(first_stop_time_forward - current_time)
        print(first_stop_time_backwards - current_time)
        print("time to this station is ", time_forward, " ", time_backwards)
    if not flag:
        print("No such station !")

first_route = list()
second_route = list()
first_route_time = list()
second_route_time = list()

first_route_time.append(0)
first_route_time.append(5)
first_route_time.append(3)
first_route_time.append(6)

first_route.append('A')
first_route.append('B')
first_route.append('C')
first_route.append('D')

second_route.append('E')
second_route.append('B')
second_route.append('F')
second_route.append('G')

second_route_time.append(0)
second_route_time.append(4)
second_route_time.append(4)
second_route_time.append(4)

station_name = ""
time_begin = 300
time_end = 2500
interval = 10
while True:
    answer = input("Enter station: ")
    # time = datetime.now().strftime("%H:%M")
    time_now = datetime.now()
    time_now = time_now.replace(second=0, microsecond=0)
    if not answer:
        break
    if find_station_name(first_route, answer):
        calculate_time(first_route, first_route_time, answer, time_now, time_begin, time_end, interval)
        # print("Now is: ", time)
        # print()
    else:
        print("No such station!")