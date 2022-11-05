from typing import Generator, IO


def _022(_in: Generator, _out: IO):
    lookup = {
        'forward': (1, 0),
        'down': (0, 1),
        'up': (0, -1),
    }

    x, y, aim = 0, 0, 0
    for i in _in:
        move, mul = i.split()
        dx, dy = lookup[move]
        x += dx * int(mul)
        y += aim * dx * int(mul)
        aim += dy * int(mul)

    num = x * y
    _out.write(str(num))
