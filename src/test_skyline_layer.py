from alg.ptwise import ptwise_gskyline
from alg.skyline_layer import skyline_layer_2d, split_layer, cal_parent_child, skyline_layer_md
from data_gen import gen_example
from entity.DSG import DSG


def test_2d(pts, k):
    skyline_layer_2d(pts, k)
    layers = split_layer(pts, k)
    cal_parent_child(layers, k)

    # print('index', 'label', 'layer', 'children')
    # for pt in pts:
    #     print(pt.index(), pt.label(), pt.layer(), pt.children())

    dsg = DSG(pts)
    groups = ptwise_gskyline(dsg, k)
    print(len(groups))


def test_md(pts, k):
    layers = skyline_layer_md(pts, k)
    cal_parent_child(layers, k)

    # print('index', 'label', 'layer', 'children')
    # for pt in pts:
    #     print(pt.index(), pt.label(), pt.layer(), pt.children())

    dsg = DSG(pts)
    groups = ptwise_gskyline(dsg, k)
    print(len(groups))


def get_pt_by_label(pts, label):
    for pt in pts:
        if pt.label() == label:
            return pt


if __name__ == '__main__':
    pts = gen_example()
    k = 4
    test_2d(pts, 4)
    pts = gen_example()
    test_md(pts, 4)


