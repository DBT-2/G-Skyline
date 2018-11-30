#coding=utf-8
from entity.Point import Point
from entity.unitGroup import unitGroup
#
def buildUnitGroup(layers,k):
    uGroups=[]
    i=k
    while i>0:
        #从最深的层数开始取点，实现重新排序
        for pt in layers[i-1]:
            #预处理，将parent数量不符合的删除掉
            if(len(pt.parents())<k):
                #
                size=1+len(pt.parents())
                pt.parents().add(pt)
                ug=unitGroup(pt,pt.parents(),size)
                uGroups.append(ug)
        i-=1
    return  uGroups
#预处理，将size为k的直接输出，并从列表弹出
def preprocess(uGroups,k):
    uDelete=[]
    for i in range(0,len(uGroups)):
        if(uGroups[i].size==k):
            print(uGroups[i])
            uDelete.append(uGroups[i])
    for group in uDelete:
        uGroups.remove(group)
    return uGroups
#计算每个group的tailSet
def cal_tail_set(uGroups):
    for i in range(0,len(uGroups)):
        uGroups[i].tailSet=uGroups[i+1:len(uGroups)]
last_num=0
#Subset Pruning for 1-unit groups
#从后往前做可以优化时间,记录一个值，这个值之后的group不用做扩展
def subset(uGroups,k):
    i=len(uGroups)-1
    while i>0:
        all = set()
        for j in range(i,len(uGroups)):
            all=uGroups[j].parent.union(all)
        if(len(all)==k):
             print all
             break
        elif(len(all)>k):
            break
        i-=1
    uGroups=uGroups[0:i]
    last_num=i
    return uGroups
#unitWise的主程序
def unitWise(uGroups,k):
    level=[]
    le=0
    #定义最高层数为k-1
    for i in range(0,k):
        level.append([])
    level[0]=uGroups
    for i in range(0,k):
        if len(level[i])!=0:
            #简化删除parent一步，每一步如果都需要将tail_set中的parent删掉，会比较耗时,可以判断如果新的group的size会更大来替换
            for uG in level[i]:
                for tail_group in uG.tailSet:
                    pt=uG.pt.append(tail_group.pt)
                    parent=uG.parent.union(tail_group.parent)
                    size=len(parent)
                    #如果点数大于k，不加入新层，相当于论文中的delete
                    if size>k:
                        pass
                    #如果点数为k，直接输出结果，不加入新层
                    elif size==k:
                        #print(unitGroup(pt,parent,size))
                        le+=1
                    #如果size比k小，分为两种情况
                    elif size<k:
                        #如果加入unit之后，size不变，说明加入的unit为原unit的parent
                        if size==uG.size:
                            pass
                        else:
                            level[i+1].append(unitGroup(pt,parent,size,tail_group.tailSet))
    return le
'''
    传入参数：layer
    输出全部的G-skyline group
'''
def unitGroupWise(layers,k):
    uGroups = buildUnitGroup(layers, k)
    uGroups = preprocess(uGroups, k)
    cal_tail_set(uGroups)
    uGroups = subset(uGroups, k)
    length = unitWise(uGroups, k)
    return length

