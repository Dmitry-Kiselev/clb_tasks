def add(x:int ,y:int):
    print('Task add called with args: {}, {}'.format(x, y))
    return x + y


def mul(x:int ,y:int):
    print('Task mul called with args: {}, {}'.format(x, y))
    return x * y


__tasks__ = [add, mul]
