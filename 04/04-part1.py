range_start = 125730
range_end   = 579381

for i in range (range_start, range_end + 1):
    digits = [int(d) for d in str(i)]
    
    never_decrease = True
    two_adjacent = False

    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            never_decrease = False
        if digits[i] == digits[i-1]:
                two_adjacent = True
        print(f'{digits} {digits[i]}')
        print(never_decrease)
        print(two_adjacent)
    break