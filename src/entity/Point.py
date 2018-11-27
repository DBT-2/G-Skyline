class Point:
    def __init__(self, index, fields, label=-1):
        self._union_group = None
        self._index = index
        self._fields = fields
        self._children = set()
        self._parents = set()
        self._is_skyline = False
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

    def index(self):
        return self._index

    def set_skyline(self, is_skyline):
        self._is_skyline = is_skyline

    def is_skyline(self):
        return self._is_skyline

    def layer(self):
        return self._layer

    def set_layer(self, layer):
        self._layer = layer

    def label(self):
        return self._label

    def union_group(self):
        if self._union_group is not None:
            return self._union_group
        else:
            self._union_group = self.cal_union_group()
            return self._union_group

    def cal_union_group(self):
        u_group = {self}
        for parent in self._parents:
            u_group = u_group.union(parent.union_group())
        return u_group

    def dominate(self, other):
        field_num = len(self._fields)
        has_less_value = False
        for i in range(0, field_num):
            if self._fields[i] > other.field_list[i]:
                return False
            elif self._fields[i] < other.field_list[i]:
                has_less_value = True
        return has_less_value

    # compare by index
    def __lt__(self, other):
        if isinstance(other, Point):
            return self._index < other.index()
        elif isinstance(other, int):
            return self._index < other
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Point):
            return self._index == other.index()
        elif isinstance(other, int):
            return self._index == other
        else:
            return False

    def __hash__(self):
        return hash(self._index)

    def __repr__(self):
        return str(self._label)
