from time import time

from conf.config import logger
from entity.SkylineGroup import SkylineGroup


def can_add(curr_group, pt):
    pts = curr_group.pts()
    parents = pt.parents()
    for parent in parents:
        if parent not in pts:
            return False
    return True


def ptwise_gskyline(dsg, k):
    logger.debug("Start point-wise group skyline...")
    # preprocess dsg
    final_groups = preprocess(dsg, k)
    logger.info("final %d groups after preprocess: %s", len(final_groups), final_groups)
    # generate level 0
    current = SkylineGroup(0)
    curr_level_groups = [current]
    next_level_groups = []
    # generate each level
    for i in range(1, k + 1):
        t = time()

        for curr_group in curr_level_groups:
            # logger.debug("current group: %s", curr_group)
            children_set = curr_group.children_set()
            max_layer = curr_group.max_layer()
            # logger.debug("children set: %s", children_set)

            t_set = curr_group.tail_set(dsg)
            # logger.debug("tail set before: %s", t_set)
            filter_tail_set(t_set, children_set, max_layer)
            # logger.debug("tail set size : %d", len(t_set))
            # logger.debug("tail set after: %s", t_set)

            for pt in t_set:
                if not can_add(curr_group, pt):
                    continue

                new_group = SkylineGroup(i)
                new_pts = set(curr_group.pts())
                new_pts.add(pt)

                # logger.debug("curr min index: %d, new index: %d", curr_group.max_index(), pt.index)
                max_index = curr_group.max_index()
                max_index = max_index if max_index > pt.index else pt.index

                # update children set and max_layer instead of recalculating them
                new_max_layer = max_layer
                if pt.layer() > new_max_layer:
                    new_max_layer = pt.layer()
                new_group.update_children_set_lazy(pt)
                new_group.set_max_layer(new_max_layer)

                new_group.set_points(new_pts)
                new_group.set_max_index(max_index)
                # logger.debug("new set: %s", new_pts)
                # logger.debug("new_min_index: %s", max_index)

                next_level_groups.append(new_group)
        curr_level_groups = next_level_groups
        next_level_groups = []
        logger.info("Level %d consumed %fs, found %d skyline groups", i, time() - t, len(curr_level_groups))
        # logger.info("Level %d : %s", i, curr_level_groups)
    for group in final_groups:
        curr_level_groups.append(group)
    return curr_level_groups


def filter_tail_set(t_set, children_set, max_layer):
    to_remove = set()
    for pt in t_set:
        if pt not in children_set and not pt.is_skyline():
            to_remove.add(pt)
        if pt.layer() - max_layer >= 2:
            to_remove.add(pt)
    for pt in to_remove:
        t_set.remove(pt)
    logger.debug("%d points filtered", len(to_remove))


def preprocess(dsg, k):
    t = time()

    pt_list = dsg.list()
    to_remove = []
    final_groups = []
    for pt in pt_list:
        u_group = pt.unit_group()
        if len(u_group) > k:
            to_remove.append(pt)
        elif len(u_group) == k:
            skyline_group = SkylineGroup(k)
            skyline_group.set_points(list(u_group))
            final_groups.append(skyline_group)
            to_remove.append(pt)

    logger.info("removed %d points because their union group sizes exceed k or beyond kth layer", len(to_remove))
    for pt in to_remove:
        pt_list.remove(pt)
    reindex(pt_list)
    dsg.set_list(pt_list)

    logger.info("preprocess consumed %fs", time() - t)
    return final_groups


def reindex(pts):
    for i in range(0, len(pts)):
        pts[i].index = i
