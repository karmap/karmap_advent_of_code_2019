range_start = 125730
range_end   = 579381

counter = 0

# def find_groups(digits):
#     for i in range(len(digits):
#         if 


for num in range (range_start, range_end + 1):
    digits = [int(d) for d in str(num)]
    
    never_decrease = True
    two_adjacent = False

    # print(num)

    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            never_decrease = False
        if digits[i+1] == digits[i]:
            two_adjacent = True
        # if i < len(digits) - 2:
        #     if digits[i+2] == digits[i+1] == digits[i]:
        #         # print(f'{digits} {digits[i]}', end=' ')
        #         # print(never_decrease, end=' ')
        #         # print(two_adjacent)
        if not never_decrease:
            break

    if never_decrease and two_adjacent:
        counter +=1
        # print(f'{digits} {digits[i]}', end=' ')
        # print(never_decrease, end=' ')
        # print(two_adjacent)

    # if num > range_start + 2:
    # if counter > 2:
    #     break
print(counter) #ans 2081