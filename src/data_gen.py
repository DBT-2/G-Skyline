from entity.Point import Point


def data_cmp(o1, o2):
    if o1[0] < o2[0]:
        return -1
    elif o1[0] == o2[0]:
        return 0
    return 1


def gen_example():
    data = [[4, 400, 1], [24, 380, 2], [14, 340, 3], [36, 300, 4], [26, 280, 5],
            [8, 260, 6], [40, 200, 7], [20, 180, 8], [34, 140, 9], [28, 120, 10],
            [16, 60, 11]]
    data.sort(data_cmp)
    # print(data)
    pts = []
    i = 0
    for d in data:
        pt = Point(i, d[0:2], d[2])
        pts.append(pt)
        i = i + 1
    return pts
