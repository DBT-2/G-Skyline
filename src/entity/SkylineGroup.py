class SkylineGroup:

    def __init__(self, level):
        self.level = level
        self._set = set()
        self._min_index = 1 << 63 - 1
        self._children_set = None
        self._max_layer = -1
        self._tail_set = None

    def add(self, point):
        self._set.add(point)
        if self._min_index > point.index():
            self._min_index = point.index()

    # point_list must be sorted by index of points
    def set_points(self, points):
        if isinstance(points, list):
            self._set = set(points)
        elif isinstance(points, set):
            self._set = points
        else:
            raise TypeError(type(points))

    def set(self):
        return self._set

    def min_index(self):
        return self._min_index

    def set_min_index(self, index):
        if index <= self._min_index:
            self._min_index = index

    def children_set(self):
        if self._children_set is None:
            self._cal_children_set()
        return self._children_set

    def set_children_set(self, c_set):
        self._children_set = c_set

    # max_layer must not be called before _max_layer is set
    def max_layer(self):
        return self._max_layer

    def set_max_layer(self, layer):
        self._max_layer = layer

    def _cal_children_set(self):
        self._children_set = set()
        for pt in self._set:
            self._children_set = self._children_set.union(pt.children())
            if pt.layer() > self._max_layer:
                self._max_layer = pt.layer()

    def tail_set(self, dsg):
        if self._tail_set is None:
            self._tail_set = self._cal_tail_set(dsg)
        return self._tail_set

    def _cal_tail_set(self, dsg):
        # TODO this can be optimized by reusing parents' tail_set?
        t_set = dsg.tail_set(self._min_index)
        t_set = set(t_set)
        for pt in self.set():
            t_set.remove(pt)
        return t_set

    def __repr__(self):
        return str(self._set)

    def __eq__(self, other):
        return self._set == other.set()

    def __hash__(self):
        # TODO optimize?
        return hash(str(self._set))
        # h = 0
        # for pt in self._set:
        #     h = h ^ pt.index()
        # return h
