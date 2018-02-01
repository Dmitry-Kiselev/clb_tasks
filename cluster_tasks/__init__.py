__tasks__ = []


def register(f):
    __tasks__.append(f)
    return f


@register
def add(x: int, y: int):
    print('Task add called with args: {}, {}'.format(x, y))
    return x + y


@register
def mul(x: int, y: int):
    print('Task mul called with args: {}, {}'.format(x, y))
    return x * y


@register
def bubble_sort(alist: list):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist
