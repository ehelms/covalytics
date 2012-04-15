import unittest

from covalytics import cov


class TestCovalytics(unittest.TestCase):

    def setUp(self):
        self.file = 'tests/fixtures/test.xml'

    def test_start(self):
        self.assertTrue(True)
