n1 = input()
lst1 = list(map(int, input().split()))
n2 = input()
lst2 = list(map(int, input().split()))
n3 = input()
lst3 = list(map(int, input().split()))


def get_nums_in_lists(list1: list, list2: list, list3: list):
    nums_set = set()
    nums_set.update(list1, list2, list3)
    ans = set()
    for num in nums_set:
        if num in list1:
            if num in list2 or num in list3:
                ans.add(num)
        elif num in list2 and num in list3:
            ans.add(num)
    print(*ans)


get_nums_in_lists(lst1, lst2, lst3)
