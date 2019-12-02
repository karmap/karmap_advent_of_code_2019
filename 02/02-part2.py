
# answer: 4945026
input_string = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0'.split(',')
input = [*map(int, input_string)]

def calc(input, noun, verb):
    input[1] = noun
    input[2] = verb
    for i in range(3,len(input),4):
        inst = input[i-3:i+1]
        #print(inst)
        if inst[3] > len(input):
            break
        if 99 in inst and (len(input)-i) < 4:
            break
        if inst[0] == 1:
            #sum
            input[inst[3]] = input[inst[1]] + input[inst[2]]
        else:
            #mult
            input[inst[3]] = input[inst[1]] * input[inst[2]]
    return input[0]

#print(calc(input,12,2))

#find 19690720
def find_case(target):
    for i in range(0,99):
        for j in range(0,99):
            input_copy = input.copy()
            res = calc(input_copy, i, j)
            if res == target:
                return f'{i}{j}'

print(find_case(19690720))
