import unittest
from unittest import TestCase

# import .test_plans
from ..test_plans import ppr_test

class MainUnitTest(TestCase):

    def test_can_set_smu_address(self):
        pprtest = ppr_test.PprTestPlan(smu1="SMUADDRESS")
        self.assertEqual(pprtest.smu1.address, "SMUADDRESS")

    def test_can_set_osa_address(self):
        pprtest = ppr_test.PprTestPlan(osa1="OSAADDRESS")
        self.assertEqual(pprtest.osa1.address, "OSAADDRESS")

# if __name__ == "__main__":
#     unittest.main()