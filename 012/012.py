from typing import Generator, IO


def _012(_in: Generator, _out: IO):
    count = 1

    _in = [x for x in _in]
    sample = 0
    for idx in range(len(_in) - 2):
        temp = sum(map(int, _in[idx:idx + 3]))
        if sample > temp:
            count += 1
        sample = temp

    _out.write(str(count))
