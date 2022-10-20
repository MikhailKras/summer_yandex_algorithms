def check_repeating(k, lst):
    nums_dict = dict()
    for pos, num in enumerate(lst):
        if num in nums_dict.keys():
            nums_dict[num].append(pos)
        else:
            nums_dict[num] = [pos]

    for num, positions in nums_dict.items():
        for i in range(len(positions)):
            if i != len(positions) - 1:
                delta = positions[i+1] - positions[i]
                if delta <= k:
                    return 'YES'

    return 'NO'


if __name__ == '__main__':
    n1, k1 = list(map(int, input().split()))
    lst1 = list(map(int, input().split()))
    print(check_repeating(k1, lst1))
