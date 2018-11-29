from entity.Point import Point
import csv


def pt_cmp(o1, o2):
    if o1.field_list()[0] < o2.field_list()[0]:
        return -1
    elif o1.field_list()[0] == o2.field_list()[0]:
        return 0
    return 1


def gen_example():
    data = [[4, 400, 1], [24, 380, 2], [14, 340, 3], [36, 300, 4], [26, 280, 5],
            [8, 260, 6], [40, 200, 7], [20, 180, 8], [34, 140, 9], [28, 120, 10],
            [16, 60, 11]]
    # print(data)
    pts = []
    i = 0
    for d in data:
        pt = Point(i, d[0:2], d[2])
        pts.append(pt)
        i = i + 1
    pts.sort(pt_cmp)
    return pts


def gen_csv(filename, size):
    data = [None] * size
    pts = [None] * size
    i = 0
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data[i] = row
            i = i + 1
            if i >= size:
                break
    data = [[float(x) for x in row] for row in data]

    i = 0
    for d in data:
        pt = Point(i, d, i)
        pts[i] = pt
        i = i + 1
    pts.sort(pt_cmp)
    return pts


if __name__ == '__main__':
    rst = gen_csv('/Users/koutakashi/codes/G-Skyline/data/anti_2.txt', 10000)
    print(rst)
