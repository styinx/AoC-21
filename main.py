import sys
import importlib

from util.io import read, write


if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = sys.argv[1]
        task = importlib.import_module(f'{num}.{num}')
        solve = task.__dict__[f'_{num}']

        solve(read(f'{num}/in'), write(f'{num}/out'))
