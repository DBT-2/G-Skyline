def pt_cmp(pt0, pt1):
    if pt0.field_list()[0] < pt1.field_list()[0]:
        return -1
    elif pt0.field_list()[0] == pt1.field_list()[0]:
        return 0
    else:
        return 1


def skyline_layer_2d(pt_list, k):
    """
    skyline_layer computes first k skyline layers of 2D points in pt_list
    :param pt_list:
    :param k:
    :return:
    """
    pt_list.sort(pt_cmp)
    pt_list[0].set_layer(0)
    pt_list[0].set_skyline(True)
    max_layer = 0
    tails = [pt_list[0]]
    n = len(pt_list)

    i = 0
    for i in range(1, n):
        if not tails[0].dominate(pt_list[i]):
            # print("%d not dom %d" % (tails[0].label(), pt_list[i].label()))
            pt_list[i].set_layer(0)
            pt_list[i].set_skyline(True)
            tails[0] = pt_list[i]
        elif tails[max_layer].dominate(pt_list[i]):
            # print("%d doms %d" % (tails[max_layer].label(), i))
            if max_layer < k:
                max_layer = max_layer + 1
                tails.append(pt_list[i])
                pt_list[i].set_layer(max_layer)
            else:
                i = i - 1
                break
        else:
            pos = bin_dom_search(tails, pt_list[i])
            # print("find pos %d for %d" % (pos, pt_list[i].label()))
            pt_list[i].set_layer(pos)
            tails[pos] = pt_list[i]
    return pt_list[:i+1]


def bin_dom_search(tails, pt):
    lo = 0
    hi = len(tails)
    while lo < hi:
        mid = (lo + hi) // 2
        if not tails[mid].dominate(pt):
            hi = mid
        else:
            lo = mid + 1
    return lo


def split_layer(pts, k):
    layers = []
    for i in range(0, k):
        layers.append([])
    for pt in pts:
        layers[pt.layer()].append(pt)
    return layers


def cal_parent_child(layers, k):
    for i in range(1, k):
        for pt in layers[i]:
            for j in range(0, i):
                for par_pt in layers[j]:
                    if par_pt.dominate(pt):
                        pt.add_parent(par_pt)
                        par_pt.add_child(pt)