# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

def path(instructions):
    coords = instructions.split(',')
    pos = [0,0,0]
    path = []
    for i in coords:
        #print(i)
        steps = int(i[1:])
        code = i[0]
        if code == 'U':
            for i in range(0, steps):
                pos[1] += 1
                pos[2] += 1 # Third dimention saves steps
                path.append(tuple(pos.copy()))  
        elif code == 'D':
            for i in range(0, steps):
                pos[1] -= 1
                pos[2] += 1 # Third dimention saves steps
                path.append(tuple(pos.copy()))  
        elif code == 'L':
           for i in range(0, steps):
                pos[0] -= 1
                pos[2] += 1 # Third dimention saves steps
                path.append(tuple(pos.copy()))      
        elif code == 'R':
            for i in range(0, steps):
                pos[0] += 1
                pos[2] += 1 # Third dimention saves steps
                path.append(tuple(pos.copy()))
    return path

def closest_intersection(a, b):
    a_cut = (tuple([x[0], x[1]]) for x in a)
    b_cut = (tuple([x[0], x[1]]) for x in b)
    return min(abs(x[0])+abs(x[1]) for x in set(a_cut).intersection(b_cut))

def inters(a, b):
    a_cut = (tuple([x[0], x[1]]) for x in a)
    b_cut = (tuple([x[0], x[1]]) for x in b)
    return list([x[0], x[1]] for x in set(a_cut).intersection(b_cut))

def less_steps(a, b, inters):
    totals = []
    for i in inters:
        current_sum = 0
        for x in a:
            if x[0] == i[0] and x[1] == i[1]:
                # print(i)
                # print(x)
                current_sum += x[2]
        for y in b:
            if y[0] == i[0] and y[1] == i[1]:
                # print(i)
                # print(y)
                current_sum += y[2]
        totals.append(current_sum)
    return min(totals)

# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83' # = distance 159

# wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51' 
# wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7' # = distance 135

f = open("03-input.txt", "r")
wire1 = f.readline()
wire2 = f.readline()

path1 = path(wire1)
path2 = path(wire2)

inters_list = inters(path1, path2)

print(len(path1))
print(len(path2))
print(len(inters_list))

print(closest_intersection(path1, path2))
print(less_steps(path1, path2, inters_list)) # ans = 16368
