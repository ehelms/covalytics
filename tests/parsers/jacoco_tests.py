import unittest

from covalytics.parsers import jacoco


class TestJacocoParser(unittest.TestCase):

    def setUp(self):
        self.file = open('tests/fixtures/test.xml', 'r')

    def tearDown(self):
        self.file.close()

    def test_parse_xml(self):
        data = jacoco.parse_xml(self.file)
        self.assertIsNotNone(data)
    
    def test_extracted_data(self):
        data = jacoco.parse_xml(self.file)
        extracted_data = jacoco.extract_data(data)
        self.assertIsNotNone(extracted_data)
