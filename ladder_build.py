url = 'https://contest.yandex.ru/contest/39359/problems/A/?success=72366328#30404/2022_08_15/6GzztTM16b'


def count_steps(n):
    steps = 0
    blocks = 1
    count = 0
    while count < n:
        count += blocks
        if count > n:
            break
        blocks += 1
        steps += 1
    return steps


n1 = int(input())
print(count_steps(n1))
