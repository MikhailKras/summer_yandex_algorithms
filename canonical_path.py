url = 'https://contest.yandex.ru/contest/39359/problems/B/?success=72370042#30404/2022_08_16/tCD0pLUaVp'


def get_can_path(path: str) -> str:
    dirs = [x for x in path.split('/') if x]
    real_dirs = []
    for i in range(len(dirs)):
        if dirs[i] == '..' and i != 0 and real_dirs:
            real_dirs.pop()
        elif dirs[i] == '.' or dirs[i] == '..':
            pass
        else:
            real_dirs.append(dirs[i])
    return '/' + '/'.join(real_dirs)


print(get_can_path('/./..'))
s = input(':')
print(get_can_path(s))

