"""Usage:
    cast compare <lift_file> <right_file>
"""
__author__ = 'V8q1ez'

from docopt import docopt


def process_compare_command(args):
    print('Files are identical')
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['compare']:
        process_compare_command(arguments)

