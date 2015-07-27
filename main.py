"""Usage:
    cast compare <left_file> <right_file>
"""
__author__ = 'V8q1ez'

from docopt import docopt
from src.castle.warlock import warlock


def process_compare_command(arguments):
    w = warlock()

    left_file = open(arguments['<left_file>'], 'r')
    right_file = open(arguments['<right_file>'], 'r')

    left_file_lines = left_file.readlines()
    right_file_lines = right_file.readlines()

    if True == w.areFilesEquivalent(left_file_lines, right_file_lines):
        print('Files are equivalent')
    else:
        print('Files are different')
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['compare']:
        process_compare_command(arguments)

