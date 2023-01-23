f = open('Lab1.txt', 'r')
map = []
a = 0
b = 0
c = []
task_closing = []
x = []

for line in f:
    map.append(line.split())


if a > b:
    for i in range(0, len(map)):
        if i == 0:
            map[i].append(a - b)
        else:
            map[i].append(0)
elif a < b:
    for i in range(0, len(map[0])):
        if i == 0:
            task_closing.append(b-a)
        else:
            task_closing.append(0)
    map.append(task_closing)


for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        map[i][j] = int(map[i][j])
        if i == 0 and j > 0:
            b += map[i][j]
        elif i > 0 and j > 0:
            c.append(map[i][j])
    if i > 0:
        a += map[i][0]


def least_path_method(mapf):
    c = []


    for i in range(0, len(mapf)):
        for j in range(0, len(mapf[0])):
            if i > 0 and j > 0 and map[i][j] != 0 and mapf[i][j] != -1:
                c.append(map[i][j])
    print(c)

    if c != []:
        for i in range(0, len(mapf)):
            if mapf[i].count(min(c)) > 0:
                line = i
                column = mapf[i].index(min(c))
                break
            else:
                line = 1
                column = 1

        print(line)
        print(column)

        if mapf[line][0] >= mapf[0][column]:
            x[(len(mapf[0]) - 1) * (line - 1) + column - 1] = mapf[0][column] * mapf[line][column]
            mapf[line][0] -= mapf[0][column]
            mapf[0][column] = 0
        else:
            x[6*(line-1)+column-1] = mapf[line][0] * mapf[line][column]
            mapf[0][column] -= mapf[line][0]
            mapf[line][0] = 0

        print(x)
        for line in mapf:
            print(line)

        for i in range(1, len(mapf[0])):
            if mapf[0][i] == 0:
                for j in range(0, len(mapf)):
                    # print(matri[j])
                    mapf[j][i] = -1
                break
        for i in range(1, len(mapf)):
            if mapf[i][0] == 0:
                for j in range(0, len(mapf[0])):
                    mapf[i][j] = -1
                break

        for line in mapf:
            print(line)

        least_path_method(mapf)
    else:
        print("\nTask complete!")
        for i in range(0, len(x)):
            print("x"+str(i) + " = " + str(x[i]))




for line in map:
    print(line)

for i in range(0, (len(map) - 1) * (len(map[0]) - 1)):
    x.append(0)

print(x)

least_path_method(map)
