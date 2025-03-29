# coding:utf-8

import os
from tempfile import TemporaryDirectory
from typing import Union
import unittest

from xkits_sheet.table import Form
from xkits_sheet.xls import Reader
from xkits_sheet.xls import Writer


class TestXLS(unittest.TestCase):

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

    def test_xls_header_sheet(self):
        with TemporaryDirectory() as thdl:
            path = os.path.join(thdl, "sheet", "test.xls")
            writer = Writer()
            writer.dump_sheet(self.fake_form)
            writer.save(path)
            reader = Reader(path)
            reader.load_sheet()
            self.assertEqual(reader.file, path)

    def test_xls_header_sheets(self):
        with TemporaryDirectory() as thdl:
            path = os.path.join(thdl, "sheets", "test.xls")
            writer = Writer()
            writer.dump_sheets([self.fake_form,
                                Form("socre2", ["name", "score2"])])
            writer.save(path)
            reader = Reader(path)
            reader.load_sheets()
            self.assertEqual(reader.file, path)


if __name__ == "__main__":
    unittest.main()
