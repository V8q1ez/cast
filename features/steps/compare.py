from behave import *
import os
import subprocess

FILE_CONTENT = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""

@given('the left and right files are completely identical')
def step_impl(context):
    left_file = open('left_file.c', 'w')
    right_file = open('right_file.c', 'w')

    left_file.write(FILE_CONTENT)
    right_file.write(FILE_CONTENT)

    left_file.close()
    right_file.close()

@when('the \'cast compare\' is performed')
def step_impl(context):
    line = 'cast.bat compare left_file.c right_file.c'
    p = subprocess.Popen(line, stdout=subprocess.PIPE, stderr=None, stdin=None)
    context.output = p.stdout.read()
    p.wait()

@then(u'the output shall contain \'Files are equivalent\'')
def step_impl(context):
    print(context.output)
    assert( str('Files are equivalent') in str(context.output) )


