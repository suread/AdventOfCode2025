from scipy.optimize import linprog

def input_to_array(file_name):
    #f = open(file_name)
    #contents = f.read()
    #f.close()
    #return contents.splitlines()
    with open(file_name) as f:
        return f.readlines()

def input_as_string(file_name):
    with open(file_name) as f:
        return f.read()

def aoc2025_1a():
    inp = input_to_array("day1a.txt")

#     inp = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".splitlines()

    point = 50
    count_zero = 0

    for move in inp:
        dirn = move[:1]  # slice syntax
        dist = int(move[1:])
        if dirn == "L":
            point -= dist
        else:
            point += dist

        while point < 0:
            point += 100
        while point > 99:
            point -= 100
        if point == 0:
            count_zero += 1

    print(count_zero)

def aoc2025_1b():
    inp = input_to_array("day1a.txt")

#     inp = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".splitlines()

    point = 50
    count_zero = 0
    print("   ", point, count_zero)

    for move in inp:
        dirn = move[:1]
        dist = int(move[1:])
        while dist > 99:
            dist -= 100
            count_zero += 1

        if dirn == "L":
            if (point - dist) == 0:
                point = 0
                count_zero += 1
            elif (point - dist) < 0:
                if point == 0:
                    point += 100 - dist
                else:
                    point += 100 - dist
                    count_zero += 1
            else:
                point -= dist
        else:
            if (point + dist) == 100:
                point = 0
                count_zero += 1
            elif (point + dist) > 100:
                if point == 0:
                    point += dist - 100
                else:
                    point += dist - 100
                    count_zero += 1
            else:
                point += dist


        print(move, point, count_zero)

    # 5828 too low

    print(count_zero)

def aoc2025_2a():
    inp = input_as_string("day2a.txt")
    # inp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    ranges = inp.split(",")

    total = 0

    for r in ranges:
        # start, end = r.split("-") - didn't use this but should work and be neater
        start = r.split("-")[0]
        end = r.split("-")[1]
        for i in range(int(start),int(end)+1):
            test = str(i)
            if len(test) % 2 == 1:
               continue
            half = int(len(test)/2)
            t1 = test[:half]
            t2 = test[half:]
            if t1 == t2:
                total += i
            # print(i, t1, t2)


    print(total)

def aoc2025_2b():
    inp = input_as_string("day2a.txt")
    # inp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    ranges = inp.split(",")

    total = 0

    for r in ranges:
        start = r.split("-")[0]
        end = r.split("-")[1]
        for i in range(int(start),int(end)+1):
            number = str(i)
            half = int(len(number)/2)
            for j in range(1, half+1):
                if len(number) % j != 0:
                    continue
                test = number[:j]

                # print(number, test, total)
                if number.count(test) == len(number) / len(test):
                    total += i
                    break


    print(total)

def aoc2025_3a():
    inp = input_to_array("day3a.txt")
#     inp = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".splitlines()

    total = 0

    for line in inp:
        max_ = 0
        for i in range(0, len(line)):
            for j in range(i+1, len(line)):

                jolt = int(line[i]+line[j])
                if jolt > max_:
                    max_ = jolt
        total += max_

    print(total)

def aoc2025_3b():
    inp = input_to_array("day3a.txt")
#     inp = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".splitlines()

    total = 0

    for line in inp:
        output = ""
        first = 0
        for i in range (0,12):
            position = -1
            largest = "0"
            for x in range(first, len(line)-11+i):
                if line[x] > largest:
                    largest = line[x]
                    position = x
            first = position+1
            output += largest

            print(line, output)
        total += int(output)

    print(total)

def aoc2025_4a():
    inp = input_to_array("day4a.txt")
#     inp = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".splitlines()

    accessible = 0
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    for i in range(len(inp)):
        for j in range (len(inp[i])):
            count = 0
            if inp[i][j] == "@":
                for direction in directions:
                    if (0 <= i+direction[0] < len(inp)) and (0 <= j+direction[1] < len(inp[i])):
                        if inp[i+direction[0]][j+direction[1]] == "@":
                            count += 1
                if count < 4:
                    accessible += 1

    print(accessible)

def aoc2025_4b():
    inp = input_to_array("day4a.txt")
#     inp = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".splitlines()

    accessible = 0
    directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    changed = True

    for i in range(len(inp)):
        inp[i] = list(inp[i].strip())
    while changed:
        changed = False
        for i in range(len(inp)):
            for j in range (len(inp[i])):
                count = 0
                if inp[i][j] == "@":
                    for direction in directions:
                        if (0 <= i+direction[0] < len(inp)) and (0 <= j+direction[1] < len(inp[i])):
                            if inp[i+direction[0]][j+direction[1]] == "@":
                                count += 1
                    if count < 4:
                        accessible += 1
                        inp[i][j] = "x"
                        changed = True

    print(accessible)

def aoc2025_5a():
    inp = input_to_array("day5a.txt")
    # inp = """3-5
    # 10-14
    # 16-20
    # 12-18
    #
    # 1
    # 5
    # 8
    # 11
    # 17
    # 32""".splitlines()

    ranges = []
    ids = []
    first = True

    for i in range(len(inp)):
        if inp[i].strip() == "":
            first = False
        elif first:
            next_ = inp[i].strip().split("-")
            ranges.append([int(next_[0]),int(next_[1])])
        else:
            ids.append(int(inp[i].strip()))

    count = 0
    for id_ in ids:
        for range_ in ranges:
            if range_[0] <= id_ <= range_[1]:
                count += 1
                break

    print(count)

def aoc2025_5b():
    inp = input_to_array("day5a.txt")
    # inp = """3-5
    # 10-14
    # 16-20
    # 12-18
    #
    # 1
    # 5
    # 8
    # 11
    # 17
    # 32""".splitlines()

    ranges = []
    ids = []
    first = True

    for i in range(len(inp)):
        if inp[i].strip() == "":
            first = False
        elif first:
            next_ = inp[i].strip().split("-")
            ranges.append([int(next_[0]),int(next_[1])])
        else:
            ids.append(int(inp[i].strip()))

    ranges.sort(key=sort5b)

    changed = True
    while changed:
        changed = False
        for i in range(1, len(ranges)):
            if ranges[i][0] <= ranges[i-1][1]:
                if ranges[i][1] > ranges[i-1][1]:
                    ranges[i - 1][1] = ranges[i][1]
                ranges.pop(i)
                changed = True
                break

    count = 0
    for range_ in ranges:
        count += range_[1] - range_[0] + 1
    print(count)

    # 300269161174263 too low
    # 338258295736104
    # 338258295736123 too high

def sort5b(e):
    return e[0]

def aoc2025_6a():
    inp = input_to_array("day6a.txt")
#     inp = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """.splitlines()

    # each element of numbers is a list comprising the integers in the row
    numbers = [[int(x) for x in inp[i].split()] for i in range(0,len(inp)-1) ]
    operations = inp[-1].split()

    total = 0
    for i in range(0,len(operations)):
        if operations[i] == "*":
            sum_ = 1
        else:
            sum_ = 0
        for j in range(0, len(numbers)):
            if operations[i] == "*":
                sum_ *= numbers[j][i]
            else:
                sum_ += numbers[j][i]
        total += sum_

    print(total)

def aoc2025_6b():
    inp = input_to_array("day6a.txt")
#     inp = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """.splitlines()

    # numbers = [[int(x) for x in inp[i].split()] for i in range(0,len(inp)-1) ]
    max_size = len(max(inp, key=len))

    numbers = [list(inp[i].ljust(max_size)) for i in range(0,len(inp)-1)]

    list(map(list, zip(*numbers)))
    transpose = list(map(list, zip(*numbers)))
    new_numbers = [''.join(a) for a in transpose]

    operations = inp[-1].split()

    total = 0
    number_pos = 0
    for i in range(0, len(operations)):
        if operations[i] == "*":
            sum_ = 1
        else: sum_ = 0

        while number_pos < len(new_numbers) and new_numbers[number_pos].strip() != "":
            if operations[i] == "*":
                sum_ *= int(new_numbers[number_pos])
            else:
                sum_ += int(new_numbers[number_pos])
            number_pos += 1
        number_pos += 1
        total += sum_
    print(total)

def aoc2025_7a():
    inp = input_to_array("day7a.txt")
#     inp = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............""".splitlines()

    paths = [list(inp[y]) for y in range(len(inp))]
    total = 0
    for y in range(1, len(paths)):
        for x in range(len(paths[0])):
            if paths[y-1][x] == "S":
                paths[y][x] = "|"
            if paths[y-1][x] == "|":
                if paths[y][x] == ".":
                    paths[y][x] = "|"
                elif paths[y][x] == "^":
                    total += 1
                    paths[y][x-1] = "|"
                    paths[y][x+1] = "|"
    print(total)

def aoc2025_7b():
    inp = input_to_array("day7a.txt")
#     inp = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............""".splitlines()

    paths = [list(inp[y]) for y in range(len(inp))]
    routes = [[0 for _ in range(len(paths[0]))] for _ in range(len(paths))]
    for y in range(1, len(paths)):
        for x in range(len(paths[0])):
            if paths[y-1][x] == "S":
                routes[y][x] = 1
            if routes[y-1][x] > 0:
                if paths[y][x] == ".":
                    routes[y][x] += routes[y-1][x]
                elif paths[y][x] == "^":
                    routes[y][x-1] += routes[y-1][x]
                    routes[y][x+1] += routes[y-1][x]
    total = sum(routes[len(routes)-1])
    print(total)

def aoc2025_8a():
    inp = input_to_array("day8a.txt")
#     inp = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".splitlines()

    connections = 1000

    # each element of numbers is a list comprising the integers in the row
    coords = [tuple([int(x) for x in inp[i].split(",")]) for i in range(0, len(inp))]

    distances = []

    for i in range(0, len(coords)):
        for j in range(i+1, len(coords)):
            distances.append(make_distance_tuple(coords[i], coords[j]))

    distances.sort(key=lambda tup:tup[0])

    circuits = []
    for i in range(connections):
        found = False
        for circuit in circuits:
            if distances[i][1] in circuit:
                circuit.add(distances[i][2])
                found = True
                break
            elif distances[i][2] in circuit:
                circuit.add(distances[i][1])
                found = True
                break
        if not found:
            new_circuit = {distances[i][1], distances[i][2]}
            circuits.append(new_circuit)

    merge = True
    while merge:
        merge = False
        for circuit in circuits:
            for circuit2 in circuits:
                if circuit2 == circuit:
                    continue
                if not circuit.isdisjoint(circuit2):
                    circuit3 = circuit.union(circuit2)
                    circuits.remove(circuit)
                    circuits.remove(circuit2)
                    circuits.append(circuit3)

                    merge = True
                    break

    circuits.sort(reverse=True, key=lambda set_:len(set_))

    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))

def aoc2025_8b():
    inp = input_to_array("day8a.txt")
#     inp = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".splitlines()

    # each element of numbers is a list comprising the integers in the row
    coords = [tuple([int(x) for x in inp[i].split(",")]) for i in range(0, len(inp))]

    distances = []

    for i in range(0, len(coords)):
        for j in range(i+1, len(coords)):
            distances.append(make_distance_tuple(coords[i], coords[j]))

    distances.sort(key=lambda tup:tup[0])

    circuits = []
    for i in range(len(distances)):
        found = False
        for circuit in circuits:
            if distances[i][1] in circuit:
                circuit.add(distances[i][2])
                found = True
                break
            elif distances[i][2] in circuit:
                circuit.add(distances[i][1])
                found = True
                break
        if not found:
            new_circuit = {distances[i][1], distances[i][2]}
            circuits.append(new_circuit)

        merge_circuits(circuits)
        if len(circuits) == 1 and len(circuits[0]) == len(coords):
            print(distances[i][1][0] * distances[i][2][0])
            break


    circuits.sort(reverse=True, key=lambda set_:len(set_))

def make_distance_tuple(coord1, coord2):
    dist_sq = (coord1[0]-coord2[0]) ** 2 + (coord1[1]-coord2[1]) ** 2 + (coord1[2]-coord2[2]) ** 2
    return dist_sq, coord1, coord2

def merge_circuits(circuits):
    merge = True
    while merge:
        merge = False
        for circuit in circuits:
            for circuit2 in circuits:
                if circuit2 == circuit:
                    continue
                if not circuit.isdisjoint(circuit2):
                    circuit3 = circuit.union(circuit2)
                    circuits.remove(circuit)
                    circuits.remove(circuit2)
                    circuits.append(circuit3)

                    merge = True
                    break

def aoc2025_9a():
    inp = input_to_array("day9a.txt")
#     inp = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3""".splitlines()

    coords = [tuple([int(b) for b in inp[a].split(",")]) for a in range(len(inp))]

    max_ = 0
    for a in range(len(coords)):
        for b in range(a+1, len(coords)):
            size = abs((1 + coords[a][0] - coords[b][0]) * (1 + coords[a][1] - coords[b][1]))
            if size > max_:
                max_ = size

    print(max_)

def aoc2025_9b():
    inp = input_to_array("day9a.txt")
#     inp = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3""".splitlines()

    coords = [tuple([int(b) for b in inp[a].split(",")]) for a in range(len(inp))]

    # with open("d9.svg", "w") as f:
    #     f.write("<svg width=\"10000\" height=\"10000\" xmlns=\"http://www.w3.org/2000/svg\">\n")
    #     f.write("<polygon points=\"")
    #     for coord in coords:
    #         f.write(str(coord[0]) + "," + str(coord[1]) + " ")
    #     f.write("\n\" style=\"fill:lime;stroke:purple;stroke-width:3\" />")
    #     f.write("</svg>")

    rects = [tuple([(1 + abs(coords[a][0] - coords[b][0])) * (1+ abs(coords[a][1] - coords[b][1])), coords[a], coords[b]]) for a in range(len(inp)) for b in range(len(inp))]
    rects.sort(key = lambda tup:tup[0], reverse = True)

    # 3015635616 too large
    # 1525812304 too small

    # from the SVG any rectangle must be above or include 48378, or below (or include) 50735
    rect_count = 0

    for rect in rects:
        if not ((rect[1][1] <= 48378 and rect[2][1] <= 48378) or (rect [1][1] >= 50375 and rect[2][1] >= 50375)):
            continue
        # print(f"<rect width=\"{abs(rect[2][0]-rect[1][0])}\" height=\"{abs(rect[2][1]-rect[1][1])}\" x=\"{min(rect[1][0],rect[2][0])}\" y=\"{min(rect[1][1],rect[2][1])}\" style=\"fill:rgb(0,0,255);stroke-width:3;stroke:red\" />")


        if rect[0] <= 1525812304: #we know this is too small as we tried this answer already
            print("missed the answer")
            exit(rect_count)

        if rect[0] > 2015635616: #we know this is too big as we tried this answer already
            continue

        candidate = True
        rect_count += 1
        for coord in coords:
            if coord[0] == rect[1][0] and coord[1] == rect[1][1]:
                continue
            if coord[0] == rect[2][0] and coord[1] == rect[2][1]:
                continue
            if (rect[1][0] < coord[0] < rect[2][0] or rect[2][0] < coord[0] < rect[1][0]) and (rect[1][1] < coord[1] < rect[2][1] or rect[2][1] < coord[1] < rect[1][1]):
                candidate = False
                # print(coord, rect[1], rect[2])
                break
            else:
                pass
        if not candidate:
            continue

        print(rect[0])
        print(f"<rect width=\"{abs(rect[2][0]-rect[1][0])}\" height=\"{abs(rect[2][1]-rect[1][1])}\" x=\"{min(rect[1][0],rect[2][0])}\" y=\"{min(rect[1][1],rect[2][1])}\" style=\"fill:rgb(0,0,255);stroke-width:3;stroke:red\" />")

        break
    print(1)

def aoc2025_10a():
    inp = input_to_array("day10a.txt")
    inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".splitlines()

    lights = []
    buttons = []
    jolts = []

    for line in inp:
        spl = line.split()
        lights.append(spl[0][-2:0:-1]) # take off the "[" at ends of string and reverse it!
        button_set = []
        for b in range(1,len(spl)-1):
            button_set.append([int(a) for a in spl[b][1:-1].split(",")])
        buttons.append(button_set)
        jolts.append([int(n) for n in spl[-1][1:-1].split(",")])

    total = 0

    for machine_number in range(len(buttons)):
        buttons_required = len(buttons[machine_number])
        desired_outcome = 0

        for j in range(len(lights[machine_number])):
            desired_outcome = desired_outcome << 1
            desired_outcome = desired_outcome | (lights[machine_number][j] == "#")

        for button_combo in range(2**len(buttons[machine_number])):
            button_count = button_combo.bit_count()
            if button_count >= buttons_required:
                continue

            state = 0
            for button_number in range(len(buttons[machine_number])):
                if (1 << button_number) & button_combo:
                    for t in buttons[machine_number][button_number]:
                        state = state ^ (1 << t)
            if state == desired_outcome:
                buttons_required = button_count

        total += buttons_required



    print(total)

def aoc2025_10b():
    inp = input_to_array("day10a.txt")
#     inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """.splitlines()

    lights = []
    buttons = []
    jolts = []

    # most different buttons on a machine is 13
    # most lights/different jolts is 10
    # largest number of jolts is 286
    max_lights = 0

    for line in inp:
        spl = line.split()
        if len(spl[0]) > max_lights:
            max_lights = len(spl[0])
        lights.append(spl[0][-2:0:-1]) # take off the "[" at ends of string and reverse it!
        button_set = []
        for b_ in range(1, len(spl) - 1):
            button_set.append([int(a_) for a_ in spl[b_][1:-1].split(",")])
        buttons.append(button_set)
        jolts.append([int(n) for n in spl[-1][1:-1].split(",")])

    total = 0

    for machine_number in range(len(buttons)):
        button_matrix = []
        for b_ in buttons[machine_number]:
            b_tmp = []
            for j in range(len(jolts[machine_number])):
                b_tmp.append((-1 if j in b_ else 0))
            button_matrix.append(b_tmp)
        button_matrix_transpose = list(map(list, zip(*button_matrix)))
        jolt_matrix = [-j for j in jolts[machine_number]]
        for i in range(len(button_matrix_transpose)):
            jolt_matrix.append(-jolt_matrix[i])
            button_matrix_transpose.append([-a for a in button_matrix_transpose[i]])

        vars_matrix = [1 for _ in buttons[machine_number]]

        # button_matrix = [[0,0,0,1],[0,1,0,1],[0,0,1,0],[0,0,1,1], [1,0,1,0], [1,1,0,0]]
    # button_matrix_transpose = [[0,0,0,0,1,1],[0,1,0,0,0,1],[0,0,1,1,1,0],[1,1,0,1,0,0],[0,0,0,0,-1,-1],[0,-1,0,0,0,-1],[0,0,-1,-1,-1,0],[-1,-1,0,-1,0,0]]
    # jolt_matrix = [3,5,4,7,-3,-5,-4,-7]


        res = linprog(vars_matrix, A_ub = button_matrix_transpose, b_ub = jolt_matrix, bounds = [0, None], integrality = 1)

        total += sum(res.x)

        # 16105 too low

    print(total)

def aoc2025_11a():
    inp = input_to_array("day11a.txt")
#     inp = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out""".splitlines()

    devices = {}

    for line in inp:
        spl = line.split(":")
        devices[spl[0]] = [a for a in spl[1].split()]

    print(d11a_next_hop("you", devices))

def d11a_next_hop(current, outputs):
    if current == "out":
        return 1
    routes = 0
    for next_ in outputs[current]:
        routes += d11a_next_hop(next_, outputs)
    return routes

def aoc2025_11b():
    inp = input_to_array("day11a.txt")
#     inp = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out""".splitlines()

    devices = {}

    for line in inp:
        spl = line.split(":")
        devices[spl[0]] = [a for a in spl[1].split()]

    print(d11b_next_hop("svr", devices, {})) # 511378159390560    !!!!!

def d11b_next_hop(current, outputs, known):
    if current in known:
        return

    if current == "out":
        known["out"] = (1, 0, 0, 0)
        return

    none = 0
    dac = 0
    fft = 0
    both = 0
    for next_ in outputs[current]:
        d11b_next_hop(next_, outputs, known)
        none += known[next_][0]
        dac += known[next_][1]
        fft += known[next_][2]
        both += known[next_][3]

    if current == "dac":
        dac += none
        none = 0
        both += fft
        fft = 0
    if current == "fft":
        fft += none
        none = 0
        both += dac
        dac = 0
    known[current] = (none, dac, fft, both)

    return both

def aoc2025_12a():
    inp = input_to_array("day12a.txt")
#     inp = """0:
# ###
# ##.
# ##.
#
# 1:
# ###
# ##.
# .##
#
# 2:
# .##
# ###
# ##.
#
# 3:
# ##.
# ###
# ##.
#
# 4:
# ###
# #..
# ###
#
# 5:
# ###
# .#.
# ###
#
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2""".splitlines()

    shapes = []
    regions = []

    for i in range(len(inp)):
        inp[i] = inp[i].strip()

    line_num = 0
    while line_num < len(inp):
        if inp[line_num] == "":
            line_num += 1
            continue
        if inp[line_num][1] == ":": # we know there are 6 shapes, so shape number is always a single digit
            default = []
            line_num += 1
            while not inp[line_num] == "":
                default.append(inp[line_num])
                line_num += 1
            shapes.append(D12Present(default))
        else:
            regions.append(D12Region(inp[line_num]))
            line_num += 1

    present_sizes = []
    for present in shapes:
        present_sizes.append(present.occupied_count)

    possible = 0
    impossible = 0
    # so, it turns out that for the problem data the presents either
    # a) don't fit because there is not enough space even if they were packed without gaps, or
    # b) they fit so easily it would be hard to pack them that inefficiently.
    # Suddenly we don't need to implement any box packing algorithms and the solution can be found very easily
    
    
    for region in regions:
        present_area = 0
        for i in range(0, len(shapes)):
            present_area += shapes[i].occupied_count * region.presents[i]
        if present_area > region.area: # impossible to fit the presents in this region, even with no gaps, so bail here.
            impossible += 1
            continue
        else:
            possible += 1
            print(present_area, region.area)

    print(possible, impossible) # yes, the answer really is that simple.

def d12_make_rotations(shape):
    all_orientations = set()
    flipped = shape
    for i in range(4):
        transposed = list(map(list, zip(*flipped)))

        for j in range(len(transposed)):
            transposed[j] = "".join(transposed[j])

        flipped = [a[::-1] for a in transposed]

        all_orientations.add(tuple(transposed))
        all_orientations.add(tuple(flipped))

    return all_orientations

class D12Region:
    def __init__(self, inp):
        spl = inp.split(":")
        self.dimensions = spl[0].split("x")
        self.presents = [int(a) for a in spl[1].split()]
        self.area = int(self.dimensions[0]) * int(self.dimensions[1])

class D12Present:
    def __init__(self, inp):
        self.all_orientations = None
        self.occupied_count = 0
        self.original = inp
        for line in inp:
            self.occupied_count += line.count("#")

    def make_rotations(self):
        self.all_orientations = set()
        flipped = self.original
        for i in range(4):
            transposed = list(map(list, zip(*flipped)))
            for j in range(len(transposed)):
                transposed[j] = "".join(transposed[j])
            flipped = [a[::-1] for a in transposed]

            self.all_orientations.add(tuple(transposed))
            self.all_orientations.add(tuple(flipped))

aoc2025_12a()




