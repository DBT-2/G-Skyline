class Point:
    def __init__(self, index, fields, label=-1):
        self._unit_group = None
        self.index = index
        self._fields = fields
        self._children = set()
        self._parents = set()
        self._layer = 0
        self._label = label
        return

    def field_list(self):
        return self._fields

    def children(self):
        return self._children

    def add_child(self, child):
        self._children.add(child)

    def parents(self):
        return self._parents

    def add_parent(self, parent):
        self._parents.add(parent)

    def is_skyline(self):
        return self._layer == 0

    def layer(self):
        return self._layer

    def set_layer(self, layer):
        self._layer = layer

    def label(self):
        return self._label

    def unit_group(self):
        if self._unit_group is not None:
            return self._unit_group
        else:
            self._unit_group = self.cal_unit_group()
            return self._unit_group

    def cal_unit_group(self):
        u_group = {self}
        for parent in self._parents:
            u_group = u_group.union(parent.unit_group())
        return u_group

    def dominate(self, other):
        field_num = len(self._fields)
        has_less_value = False
        for i in range(0, field_num):
            if self._fields[i] > other.field_list()[i]:
                return False
            elif self._fields[i] < other.field_list()[i]:
                has_less_value = True
        return has_less_value

    # compare by index
    def __lt__(self, other):
        if isinstance(other, Point):
            return self.index < other.index
        elif isinstance(other, int):
            return self.index < other
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Point):
            return self._label == other._label
        elif isinstance(other, int):
            return self._label == other
        else:
            return False

    def __cmp__(self, other):
        o_idx = 0
        if isinstance(other, Point):
            o_idx = other._label
        elif isinstance(other, int):
            o_idx = other
        else:
            raise TypeError(type(other))
        if self._label < o_idx:
            return -1
        elif self._label == o_idx:
            return 0
        else:
            return 1

    def __hash__(self):
        return hash(self._label)

    def __repr__(self):
        return str(self._label)
