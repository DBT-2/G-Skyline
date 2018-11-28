import bisect


class DSG:
    def __init__(self, lst):
        self._list = lst
        return

    def list(self):
        return self._list

    def set_list(self, lst):
        self._list = lst

    # return a set that contains all points whose index > index
    def tail_set(self, index):
        # # special case of root node
        # if index == 1 << 63 - 1:
        #     return self._list

        i = bisect.bisect_left(self._list, index + 1)
        if i < 0:
            return self._list
        elif 0 <= i < len(self._list):
            return self._list[i:]
        else:
            return []

