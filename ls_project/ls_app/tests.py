""" Test Cases """
from django.test import TestCase
from .apps import LsAppConfig


# Create your tests here.
class TestViews(TestCase):
    """ Views Test Class """

    @classmethod
    def setUpClass(cls):
        """ Setup class runs when the testview class starts """

    @classmethod
    def tearDownClass(cls):
        """ Teardown class runs when the testview class ends """

    def setUp(self):
        """Setup self runs on each test run"""

    def tearDown(self):
        """tearDown self runs on each test end"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_app_class(self):
        """ Test apps class """
        # appn = LsAppConfig.name
        self.assertEqual((LsAppConfig.name), "ls_app")
