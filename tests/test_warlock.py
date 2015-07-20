__author__ = 'V8q1ez'

import unittest

from src.castle.warlock import warlock


class warlockTest(unittest.TestCase):
    def setUp(self):
       pass

    def test_files_equivalent(self):
        w = warlock()

        left_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        right_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_different_functions_name(self):
        w = warlock()

        left_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        right_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo_(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

    def test_different_variable_name(self):
        w = warlock()

        left_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        right_file_text = """
#include "stdio.h"

#define a (124)

static int x = 4;

static void foo(int b)
{
    x = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

    def test_different_file_included(self):
        w = warlock()

        left_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        right_file_text = """
#include "stdlib.h"

#define a (124)

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

