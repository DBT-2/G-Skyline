#coding=utf-8
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
    return data

print(gen_example())