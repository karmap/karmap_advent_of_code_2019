range_start = 125730
range_end   = 579381

counter = 0

def get_groups(digits):
    groups = {}
    count = 1

    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            count += 1
        elif count > 1:
            groups.update( {digits[i] : count} )
            count = 1
        else:
            count = 1
        # print(f'i{i} - {digits[i+1]} {count}')
    if count > 1:
        groups.update( {digits[i] : count} )
    return groups

def num_met_criteria(digits):
    groups = get_groups(digits)
    # at least one group with 2 items
    for key, val in groups.items():
        if val == 2:
            return True
    else:
        return False


for num in range (range_start, range_end + 1):
    digits = [int(d) for d in str(num)]
    
    never_decrease = True
    two_adjacent = False

    # print(num)

    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            never_decrease = False
        if not never_decrease:
            break

    if never_decrease and num_met_criteria(digits):
        counter +=1
        # print(f'{digits} {digits[i]}', end=' ')
        # print(never_decrease, end=' ')
        # print(two_adjacent)

    # if num > range_start + 2:
    # if counter > 10:
    #     break
print(counter) #ans 1411