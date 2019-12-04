# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

def path(instructions):
    coords = instructions.split(',')
    pos = [0,0]
    path = []
    for i in coords:
        #print(i)
        steps = int(i[1:])
        code = i[0]
        if code == 'U':
            for i in range(0, steps):
                pos[1] += 1
                path.append(tuple(pos.copy()))  
        elif code == 'D':
            for i in range(0, steps):
                pos[1] -= 1
                path.append(tuple(pos.copy()))  
        elif code == 'L':
           for i in range(0, steps):
                pos[0] -= 1
                path.append(tuple(pos.copy()))      
        elif code == 'R':
            for i in range(0, steps):
                pos[0] += 1
                path.append(tuple(pos.copy()))
    return path

def closest_intersection(a, b):
    return min(abs(x[0])+abs(x[1]) for x in set(a).intersection(b))


# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83' # = distance 159

# wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51' 
# wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7' # = distance 135

f = open("03-input.txt", "r")
wire1 = f.readline()
wire2 = f.readline()

print(wire1)
print(wire2)

print(closest_intersection(path(wire1), path(wire2)))
