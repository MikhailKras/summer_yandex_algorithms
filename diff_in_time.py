def get_min_time(times: list[str]) -> int:
    if len(times) == 1:
        return 24*60
    times = [int(time[:2]) * 60 + int(time[3:]) for time in times]
    times.sort()
    min_time = min(times[0] + 24*60 - times[-1], times[-1] - times[0])
    for i in range(len(times)):
        if i != len(times) - 1:
            if times[i+1] - times[i] < min_time:
                min_time = times[i+1] - times[i]
    return min_time


lst = ['23:59', '00:00']
print(get_min_time(lst))


