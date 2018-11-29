#coding=utf-8

class Point:
    def __init__(self, index, fields):
        #unitGroup的概念
        self._unit_group = None
        #Point的顺序
        self._index = index
        #Point的维度
        self._fields = fields
        #Point的父亲节点和孩子节点
        self._children = set()
        self._parents = set()
        #Point的层次
        self._layer = 0
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
    #判断是否是全局的skyline
    def is_skyline(self):
        return self._layer == 0

    def layer(self):
        return self._layer

    def set_layer(self, layer):
        self._layer = layer

    def unit_group(self):
        if self._unit_group is not None:
            return self._unit_group
        else:
            self._unit_group = self.cal_unit_group()
            return self._unit_group
    #递归调用parent集合计算unitGroup
    def cal_unit_group(self):
        u_group = {self}
        for parent in self._parents:
            u_group = u_group.union(parent.unit_group())
        return u_group
    #定义dominate关系
    def dominate(self, other):
        field_num = len(self._fields)
        has_less_value = False
        for i in range(0, field_num):
            if self._fields[i] > other.field_list()[i]:
                return False
            elif self._fields[i] < other.field_list()[i]:
                has_less_value = True
        return has_less_value

    def __repr__(self):
        return str(self._index)+','+str(self._fields[0])
