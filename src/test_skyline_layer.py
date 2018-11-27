from alg.ptwise import ptwise_gskyline
from alg.skyline_layer import skyline_layer_2d, split_layer, cal_parent_child
from entity.DSG import DSG
from entity.Point import Point


def data_cmp(o1, o2):
    if o1[0] < o2[0]:
        return -1
    elif o1[0] == o2[0]:
        return 0
    return 1


def get_pt_by_label(pts, label):
    for pt in pts:
        if pt.label() == label:
            return pt


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

k = 4
pts = skyline_layer_2d(pts, k)
layers = split_layer(pts, k)
cal_parent_child(layers, k)

print('index', 'label', 'layer', 'children')
for pt in pts:
    print(pt.index(), pt.label(), pt.layer(), pt.children())

dsg = DSG(pts)
groups = ptwise_gskyline(dsg, 4)
print(len(groups))