#!/usr/bin/env python

"""
Tests for `annotation_exporter` package.

Call with
(venv) C:\Users\Medion\Documents\annotation_exporter>python -m unittest tests.test_ending_present

"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/annotation_exporter')))


from src.annotation_exporter.main import ending_present
#from src.annotation_exporter.annot_export import AnnotationExporter


class TestAnnotation_exporter(unittest.TestCase):
    """
    Tests for `annotation_exporter` package.
    """

    def setUp(self):
        """
        Set up test fixtures, if any.
        """
        self.s1 = ending_present('abc/doc.pdf', 'pdf')
        self.s2 = ending_present('abc/doc', 'xlsx')
        self.s3 = ending_present('abc/doc.xlsx', 'xlsx')

    def tearDown(self):
        """
        Tear down test fixtures, if any.
        """
        del self.s1
        del self.s2
        del self.s3

    def test_000_ending_present(self):
        """
        Test the function ending_present()
        """
        self.assertEqual(True, self.s1)
        self.assertEqual(False, self.s2)
        self.assertEqual(True, self.s3)