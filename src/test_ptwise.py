from alg.ptwise import ptwise_gskyline
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

label_pts = [None]
for i in range(1, 12):
    label_pts.append(get_pt_by_label(pts, i))

edges = [[6, 3], [3, 2], [8, 2], [11, 8], [11, 10], [6, 5],
         [8, 5], [10, 9], [8, 7], [5, 4], [9, 4], [9, 7]]
for edge in edges:
    label_pts[edge[0]].add_child(label_pts[edge[1]])
    label_pts[edge[1]].add_parent(label_pts[edge[0]])

layers = [[1, 6, 11], [3, 8, 10], [2, 5, 9], [4, 7]]
layer_num = 0
for layer in layers:
    for pt in layer:
        label_pts[pt].set_layer(layer_num)
        if layer_num == 0:
            label_pts[pt].set_skyline(True)
    layer_num = layer_num + 1

dsg = DSG(pts)
groups = ptwise_gskyline(dsg, 4)
print(len(groups))
