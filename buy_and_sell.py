def get_num_days_slow(prices: list) -> tuple:
    diff = 0
    n1 = 0
    n2 = 0
    budget = 1000
    for i in range(len(prices)):
        spend = budget // prices[i] * prices[i]
        gas_cubes = budget // prices[i]
        for j in range(i+1, len(prices)):
            income = gas_cubes * prices[j]
            if income - spend > diff and prices[i] <= 1000:
                diff = income - spend
                n1 = i
                n2 = j
    if not n1 and not n2:
        return n1, n2
    return n1+1, n2+1


def get_num_days_fast(prices: list) -> tuple:
    budget = 1
    res = 0, 0
    max_diff = 0
    gas_cubes = budget / prices[0]
    min_day = 0
    for i in range(1, len(prices)):
        if gas_cubes * prices[i] - budget > max_diff:
            max_diff = gas_cubes * prices[i] - budget
            res = min_day + 1, i + 1
        if budget / prices[i] > gas_cubes:
            gas_cubes = budget / prices[i]
            min_day = i
    return res


# n = input()
# lst = list(map(int, input().split()))
if __name__ == '__main__':
    lst = [10, 3, 5, 3, 11, 9]
    print(f'get_num_days_slow={get_num_days_slow(lst)}')
    print(f'get_num_days_fast={get_num_days_slow(lst)}')

