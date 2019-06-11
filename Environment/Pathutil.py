import argparse
import os


class PathComponent:

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display information about the PATH')
    parser.add_argument('--sort', dest='sort', action='store_true', help='Sort the path components alphabetically ('
                                                                         'case insensitive)')
    parser.add_argument('--showdups', dest='showdups', action='store_true', help='Highlight duplicates in path')
    args = parser.parse_args()

    env = os.environ
    path = env['PATH']
    if args.sort:
        components = sorted(path.split(sep=';'), key=lambda s: s.lower())
    else:
        components = path.split(sep=';')

    for x in components:
        print(x)



