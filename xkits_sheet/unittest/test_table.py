# coding:utf-8

from tempfile import TemporaryDirectory
from typing import Union
import unittest

from xkits_sheet.table import Cell
from xkits_sheet.table import Form
from xkits_sheet.table import Row
from xkits_sheet.table import tabulate


class TestTable(unittest.TestCase):

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

    def test_form(self):
        row = self.fake_form.new_row(["frank", 60])
        row.extend([None, 50])
        row.append("good")
        row[4] = "bad"
        self.fake_form[2] = row
        row[0].value = "garry"
        self.assertEqual(len(row), 5)
        self.assertFalse(row[3].empty)
        self.assertEqual(str(row[1]), "60")
        self.assertEqual(row[4].value, "bad")
        self.assertEqual(self.fake_form[2], row)
        self.assertEqual(len(self.fake_form), 3)
        self.assertEqual(self.fake_form.new_map(),
                         {"name": None, "score": None})
        self.assertEqual(self.fake_form.column_no("name"), 0)
        self.assertEqual(self.fake_form.column_no("score"), 1)

    def test_form_sort(self):
        def handle(items: Row[str, Union[str, int]]) -> Cell[Union[str, int]]:
            return items[1]
        self.fake_form.sort(handle)

    def test_tabulate(self):
        print(tabulate(self.fake_form))


if __name__ == "__main__":
    unittest.main()
