import argparse
import os
from colorama import Fore, Back, Style, init

class PathComponent:
    '''Class which encapsulates a component of the PATH environment variable.'''

    def __init__(self, name):
        '''Initialize with component name'''
        self.name = name
        self.is_duplicate = False

    def check_duplicate(self, other):
        '''Mark this as duplicate if other has matching name'''
        if self.name.lower() == other.name.lower():
            self.is_duplicate = True

    def print(self):
        '''Print component'''
        col = Fore.LIGHTCYAN_EX
        if self.is_duplicate:
            col = Fore.RED
        print(col + self.name)

if __name__ == '__main__':
    init(convert=True)
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

    component_list = [PathComponent(i) for i in components if len(i) > 0]

    if args.showdups:
        for n in range(0, len(component_list) - 1):
            for x in range(n + 1, len(component_list)):
                component_list[x].check_duplicate(component_list[n])

    for x in component_list:
        x.print()



