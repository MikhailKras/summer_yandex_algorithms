def get_majority(n, lst):
    dct = dict()
    for num in lst:
        if num in dct.keys():
            dct[num] += 1
            if dct[num] > int(n / 2):
                return num
        else:
            dct[num] = 1


if __name__ == '__main__':
    n1 = int(input())
    lst1 = list(map(int, input().split()))
    print(get_majority(n1, lst1))
