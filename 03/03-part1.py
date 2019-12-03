# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135


def path(instructions):
    coords = instructions.split(',')
    pos = [0,0]
    path = []
    for i in coords:
        #print(i)
        steps = int(i[1:])
        code = i[0]
        if code == 'U':
            pos[1] += steps
        elif code == 'D':
            pos[1] -= steps
        elif code == 'L':
            pos[0] -= steps
        elif code == 'R':
            pos[0] += steps
        path.append(tuple(pos.copy()))
    print(path)
    return path

def closest_intersection(a, b):
    return set(a).intersection(b)


wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

print(closest_intersection(path(wire1), path(wire2)))
