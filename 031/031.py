from typing import Generator, IO


def _031(_in: Generator, _out: IO):
    freq = None
    samples = 0
    for i in _in:
        if not freq:
            freq = [0] * len(i)
        for idx, bit in enumerate(i):
            freq[idx] += int(bit)
        samples += 1

    epsilon = ''
    gamma = ''
    for f in freq:
        if f < samples / 2:
            epsilon += '0'
            gamma += '1'
        else:
            epsilon += '1'
            gamma += '0'

    num = int(epsilon, 2) * int(gamma, 2)
    _out.write(str(num))
