import unittest

from covalytics.tests.parsers.jacoco_tests import TestJacocoParser


def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJacocoParser)
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJournalSearch))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSpreadsheet))
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestSpreadsheet)
    unittest.TextTestRunner(verbosity=2).run(suite)
