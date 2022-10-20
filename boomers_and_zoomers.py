def nums_invitations(ages: list) -> int:
    ages.sort(reverse=True)
    y = 1
    cnt_invitation = 0
    for x in range(len(ages)-1):
        while y < len(ages) and ages[x] >= ages[y] and ages[x] + 14 < 2 * ages[y]:
            cnt_invitation += 1
            if ages[y] == ages[x] and x != y:
                cnt_invitation += 1
            y += 1
    return cnt_invitation


if __name__ == '__main__':
    n = input()
    lst = list(map(int, input().split()))
    print(nums_invitations(lst))
