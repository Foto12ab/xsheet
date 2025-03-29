# coding:utf-8

import os
from tempfile import TemporaryDirectory
from typing import Union
import unittest

from xkits_sheet.csv import CSV
from xkits_sheet.table import Form


class TestCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TemporaryDirectory()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.fake_form: Form[str, Union[str, int]] = Form(
            "scores", ["name", "score"])
        self.fake_form.extend([["alice", 90], ["cindy", 80]])
        self.fake_form.append(["eric", 70])

    def tearDown(self):
        pass

    def test_csv_header(self):
        with TemporaryDirectory() as thdl:
            path = os.path.join(thdl, "test.csv")
            CSV.dump(path, self.fake_form)
            CSV.load(path)

    def test_csv_no_header(self):
        self.fake_form.header = []
        with TemporaryDirectory() as thdl:
            path = os.path.join(thdl, "test.csv")
            CSV.dump(path, self.fake_form)
            CSV.load(path, include_header=False)


if __name__ == "__main__":
    unittest.main()
