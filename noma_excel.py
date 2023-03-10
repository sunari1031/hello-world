#-*- coding: utf-8 -*-

# noma_excel.py
# class for excel
# author: noma@neople.co.kr
# last modified date: 2019.04.17

# history
# 2019.01.31
# created this file

# 2019.03.20
# added read_excel()
# changed excel writer library from xlwt to xlsxwriter because of supporting xlsx

# 2019.04.17
# added set_font_size() in write_excel()
# default font size = 10

## an example to use it ####################################################################################################################
# import noma_excel
#
# file_name = "excel_test.xlsx"
# sheet_list = ["S1", "S2"]
# subject_list = [["S1_S1", "S1_S2"], ["S2_S1", "S2_S2", "S2_S3"]]
# content_list = [[["S1_C1_a", "S1_C1_b"], ["S1_C2_a", "S1_C2_b"]], [["S2_C1_a", "S2_C1_b", "S2_C1_c"], ["S2_C2_a", "S2_C2_b", "S2_C2_c"]]]
# col_width_list = [[50, 20], [50, 20, 20]]
#
# excel = noma_excel.Excel()
# excel.write_excel(file_name, sheet_list, subject_list, content_list, col_width_list=col_width_list)
############################################################################################################################################


import xlrd         # read for excel
import xlsxwriter   # write for excel

class Excel:
    def __init__(self):
        return

    def read_excel(self, file_name):
        # excel e.g
        # sheet1
        # a b c
        # 1 2 3
        # sheet2
        # 1 2
        # a b
        # sheet_list e.g.
        # [[['a', 'b', 'c'], [1.0, 2.0, 3.0]], [[1.0, 2.0], ['a', 'b']]]
        sheet_list = []
        workbook = xlrd.open_workbook(filename=file_name)
        for sheet in workbook.sheets():
            row_list = []
            for row_index in range(sheet.nrows):
                row = sheet.row(row_index)
                col_list = []
                for col_index in row:
                    #print(col_index.value)
                    col_list.append(col_index.value)
                row_list.append(col_list)
            sheet_list.append(row_list)
        return sheet_list

    def write_excel(self, file_name, sheet_list, subject_list, content_list, col_width_list=None):
        workbook = xlsxwriter.Workbook(file_name)
        
        # add format for subject cells
        subject_format = workbook.add_format()
        subject_format.set_bold()
        subject_format.set_border()
        subject_format.set_align('center')
        subject_format.set_align('vcenter')
        subject_format.set_font_size(10)

        # add format for content cells
        content_format = workbook.add_format()
        content_format.set_border()
        content_format.set_align('center')
        content_format.set_align('vcenter')
        content_format.set_font_size(10)

        worksheet_list = []
        for sheet_cnt in range(0, len(sheet_list)):
            # add sheet on the excel
            worksheet_list.append(workbook.add_worksheet(sheet_list[sheet_cnt]))

            # add subject on the sheet
            for col_cnt in range(0, len(subject_list[sheet_cnt])):
                worksheet_list[sheet_cnt].write(0, col_cnt, subject_list[sheet_cnt][col_cnt], subject_format)

            # add content on the sheet
            for row_cnt in range(0, len(content_list[sheet_cnt])):
                for col_cnt in range(0, len(content_list[sheet_cnt][row_cnt])):
                    # start excel A2 because A1 is for subject
                    worksheet_list[sheet_cnt].write(row_cnt+1, col_cnt, content_list[sheet_cnt][row_cnt][col_cnt], content_format)

            # set col width
            for col_cnt in range(0, len(subject_list[sheet_cnt])):
                if col_width_list is None:
                    # set col width as default val if it's None
                    worksheet_list[sheet_cnt].set_column(col_cnt, col_cnt, 20)
                else:
                    worksheet_list[sheet_cnt].set_column(col_cnt, col_cnt, col_width_list[sheet_cnt][col_cnt])

        workbook.close()

'''
if __name__ == "__main__":
    file_name = "excel_test.xlsx"
    sheet_list = ["S1", "S2"]
    subject_list = [["S1_S1", "S1_S2"], ["S2_S1", "S2_S2", "S2_S3"]]
    content_list = [[["S1_C1_a", "S1_C1_b"], ["S1_C2_a", "S1_C2_b"]], [["S2_C1_a", "S2_C1_b", "S2_C1_c"], ["S2_C2_a", "S2_C2_b", "S2_C2_c"]]]
    col_width_list = [[50, 20], [50, 20, 20]]

    excel = Excel()
    excel.write_excel(file_name, sheet_list, subject_list, content_list, col_width_list=col_width_list)    
'''
