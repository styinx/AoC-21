from typing import Generator, IO


def _011(_in: Generator, _out: IO):
    count = 1

    it = _in
    cur = next(it)
    for i in it:
        if i > cur:
            count += 1
        cur = i

    _out.write(str(count))
