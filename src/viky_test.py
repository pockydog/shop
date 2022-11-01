# About excel
from openpyxl import Workbook


class Test:
    @classmethod
    def create(cls):
        """新增空白excel"""
        filename = 'xxxx.xlsx'
        excel_file = Workbook()
        excel_file.save(filename)

    @classmethod
    def put_info(cls):
        """新增工作表並指定放置位置"""




