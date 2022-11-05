def read(file: str):
    for line in open(file, 'r'):
        yield line.strip()


def write(file: str):
    return open(file, 'w')
