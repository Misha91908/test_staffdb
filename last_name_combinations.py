combinations = []

min_sum = 2
first_val = 2
last_val = 2
summ = 8
div = summ // min_sum


def compute_pattern(summ):
    _first_val = 2
    _last_val = summ - _first_val
    comb = []
    for i in range(summ - 3):
        comb.append([_first_val, _last_val])
        _first_val += 1
        _last_val -= 1
    return comb


if summ % min_sum == 0:
    combinations.append([2 for i in range(div)])
else:
    for i in range(div):
        combinations.append([2 for j in range(div)])
        combinations[-1][i] = 3

sum_mod = summ - first_val
for i in reversed(range(div)):
    print(i)
    while sum_mod > 2:
        _sum_mod = sum_mod
        c = []
        if sum_mod > 3:
            c.append(compute_pattern(sum_mod))
            for j in range(1, _sum_mod):
                # combinations.append([])
                # combinations[-1].append(first_val)
                while _sum_mod > 3:
                    _sum_mod -= 1
                    if _sum_mod > 3:
                        c.append(compute_pattern(_sum_mod))
        if len(c) > 0:
            pass
        else:
            combinations.append([first_val, sum_mod])
        sum_mod -= 1
        last_val += 1
        print(c)
    first_val += 1
    sum_mod = summ - first_val

print(combinations, '\n', len(combinations))
