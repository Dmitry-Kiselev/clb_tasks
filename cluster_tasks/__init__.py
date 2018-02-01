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
