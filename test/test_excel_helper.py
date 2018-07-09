import unittest
from base.excel_helper import ExcelHelper


class test_ExcelHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_bootstrap(self):
        excel_helper = ExcelHelper()
        excel_helper.insert_data(['2', '3', '4', '5', '6', '7'])


if __name__ == '__main__':
    unittest.main()
