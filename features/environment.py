import os

def after_scenario(context, scenario):
    os.remove('left_file.c')
    os.remove('right_file.c')