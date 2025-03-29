# coding:utf-8

import os
from tempfile import TemporaryDirectory
import unittest

from xkits_sheet.xlsx import XLSX


class TestXLSX(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TemporaryDirectory()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xlsx_load_sheets(self):
        path = os.path.join("xkits_sheet", "unittest", "example.xlsx")
        reader = XLSX(path)
        reader.load_sheets()
        self.assertEqual(reader.file, path)

    def test_xlsx_load_sheet(self):
        path = os.path.join("xkits_sheet", "unittest", "example.xlsx")
        reader = XLSX(path)
        reader.load_sheet()


if __name__ == "__main__":
    unittest.main()
