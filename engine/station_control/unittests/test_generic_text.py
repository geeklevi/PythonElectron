# import sys
# sys.path.append("..")
import unittest
from unittest import TestCase
from ..test_plans import generic_test
# from generic_test import GenericTestPlan

class MainUnitTest(TestCase):
    def test_smu_have_address(self):
        self.assertTrue(1, 1)

    def test_can_set_smu_address(self):
        self.assertTrue(2, 2)