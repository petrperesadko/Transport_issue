list_of_lists = []
with open('data.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        list_of_lists.append(inner_list)
print(list_of_lists[0][1])
s = list_of_lists[0][1]
s = s.split(':')
print(s[0])
some_list = list_of_lists[0]
some_route = list()
some_route_time = list()
some_route_time.append(0)
for i in range(4, len(some_list), 2):
    some_route.append(some_list[i])
for i in range(5, len(some_list), 2):
    some_route_time.append(int(some_list[i]))
print(some_route)
print(some_route_time)
