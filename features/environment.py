import os

def after_all(context):
    os.remove('left_file.c')
    os.remove('right_file.c')