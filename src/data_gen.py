#coding=utf-8
from entity.Point import Point
import csv

#在第一维度进行排序的cmp函数
def data_cmp(o1, o2):
    if o1[0] < o2[0]:
        return -1
    elif o1[0] == o2[0]:
        return 0
    return 1

#使用hotel给出的数据集进行测试
def gen_example():

    data = [[4, 400, 1], [24, 380, 2], [14, 340, 3], [36, 300, 4], [26, 280, 5],
            [8, 260, 6], [40, 200, 7], [20, 180, 8], [34, 140, 9], [28, 120, 10],
            [16, 60, 11]]
    data.sort(data_cmp)
    # print(data)
    pts = []
    i = 0
    for d in data:
        pt = Point(i, d[0:2])
        #print pt
        pts.append(pt)
        i = i + 1
    return pts

#读取指定size为行数的文件名的文件生成点并排序
def gen_csv(filename, size):
    #TODO 可能不需要指定长度？使用append应该可以指定
    data = [None] * size
    pts = [None] * size
    i = 0
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data[i] = row
            i = i + 1
            #TODO 可能不需要这个if判断？当读到文件尾应该会默认停止
            if i >= size:
                break
    data = [[float(x) for x in row] for row in data]
    data.sort(data_cmp)

    i = 0
    for d in data:
        #TODO 生成点的时候，index和label相同的话，是不是可以废除label属性
        pt = Point(i, d)
        pts[i] = pt
        i = i + 1
    return pts


if __name__ == '__main__':
    rst = gen_csv('/Users/tianyu/PycharmProjects/G-Skyline/datasets/anti_2.txt', 10000)

    print(rst)
