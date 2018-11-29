from alg.skyline_layer import skyline_layer_2d, split_layer, cal_parent_child, skyline_layer_md
from data_gen import gen_example, gen_csv
from entity.DSG import DSG


def test_2d(pts, k):
    pts = skyline_layer_2d(pts, k)
    reindex(pts)
    layers = split_layer(pts, k)
    cal_parent_child(layers, k)

    # print('index', 'label', 'layer', 'children')
    # for pt in pts:
    #     print(pt.index, pt.label(), pt.layer(), pt.children())

    dsg = DSG(pts)


def test_md(pts, k):
    layers, pts = skyline_layer_md(pts, k)
    reindex(pts)
    cal_parent_child(layers, k)

    # print('index', 'label', 'layer', 'children')
    # for pt in pts:
    #     print(pt.index, pt.label(), pt.layer(), pt.children())

    dsg = DSG(pts)



def get_pt_by_label(pts, label):
    for pt in pts:
        if pt.label() == label:
            return pt


def reindex(pts):
    for i in range(0, len(pts)):
        pts[i].index = i


if __name__ == '__main__':
    k = 4
    pts = gen_csv('/Users/tianyu/PycharmProjects/G-Skyline/datasets/anti_2.txt', 10000)
    pts=skyline_layer_2d(pts,k)
    layers=split_layer(pts,k)
    cal_parent_child(layers,k)
    print(layers)
    pts = gen_example()
    test_md(pts, 4)


