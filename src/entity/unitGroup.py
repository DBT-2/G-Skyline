#coding=utf-8
from entity.Point import Point

class unitGroup:
    def __init__(self,pt,parent,size,tailSet=None):
        #self.index=index
        self.pt=[pt]
        # 这里的parent做了一个小的化简，因为自身肯定不会在自己的tail set中
        self.parent=parent
        self.size=size
        self.tailSet=tailSet


    def __repr__(self):
        return '<'+str(self.parent)+','+str(self.size)+'>'