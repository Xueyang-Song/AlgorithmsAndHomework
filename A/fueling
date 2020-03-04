# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # num 加油的次数
    num = 1
    s = 0
    j = 1
    # stops 总加油站个数
    for i in range(1, len(stops)):
        if stops[i] - stops[i - 1] > m:
            num = -1
            return num
        elif d <= m:
            num = 0
            return num
    while j < len(stops):
        distance = stops[j] - stops[j - 1]
        s += distance
        if s >= m:
            s = stops[j]
            num += 1
        j += 1
    return num


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
