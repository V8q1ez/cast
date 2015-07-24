__author__ = 'V8q1ez'

import unittest

from src.castle.warlock import warlock


class warlockTest(unittest.TestCase):
    def setUp(self):
        self.left_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4;
/*
* Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""

    def test_files_equivalent(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4;
/*
* Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_different_functions_name(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4;
/*
* Multi line comment
*/
static void foo_(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

    def test_different_variable_name(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int x = 4;
/*
* Multi line comment
*/
static void foo(int b)
{
    x = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

    def test_different_variable_value(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 5;
/*
* Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( False, areFilesEquivalent )

    def test_different_single_line_comment(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // different single line comment

static int v = 4;
/*
* Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_different_multi_line_comment(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4;
/*
* Different Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_one_more_single_line_comment_right(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4; // one more single line comment
/*
* Different Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_one_more_single_line_comment_left(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124)

static int v = 4;
/*
* Different Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_one_more_multi_line_comment_right(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"
/*
 One more multi lime comment
*/
#define a (124) // single line comment

static int v = 4;
/*
* Different Multi line comment
*/
static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )

    def test_one_more_multi_line_comment_left(self):
        w = warlock()
        right_file_text = """
#include "stdio.h"

#define a (124) // single line comment

static int v = 4;

static void foo(int b)
{
    v = b * a;
}

"""
        areFilesEquivalent = w.areFilesEquivalent(self.left_file_text.splitlines(), right_file_text.splitlines())
        self.assertEqual( True, areFilesEquivalent )