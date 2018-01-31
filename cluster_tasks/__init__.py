def add(x ,y):
    print('Task add called with args: {}, {}'.format(x, y))
    return x + y


def mul(x ,y):
    print('Task mul called with args: {}, {}'.format(x, y))
    return x * y


__tasks__ = [add, mul]
