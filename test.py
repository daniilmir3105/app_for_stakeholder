import xlrd
import xlwt
import os

arr = ['Daniil', 'Miroshnichenko', 'Student', 'Peter the Great Polytechnical University', '89052325046', 'высокий', 'вовлеченность', 'прибыль', 'успех', 'союзники', 'высокий', 'безпроблемный', 'высокая']

try:
    path = os.path.abspath(__file__)
    # print(path)
    rb = xlrd.open_workbook(r"C:\Users\lenovo\OneDrive - Peter the Great St. Petersburg Polytechnical University\Документы\Daniil\programming\python\projects\app_for_stakeholder\example.xls",formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
    for c_el in row:
        print(c_el)
except FileNotFoundError as arr:
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    font1 = xlwt.Font()
    font1.name = 'Times New Roman'
    font1.colour_index = 2
    font1.bold = False

    style0 = xlwt.XFStyle()
    style0.font = font0

    style1 = xlwt.XFStyle()
    style1.font = font1

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 'Имя', style0)
    ws.write(0, 1, 'Фамилия', style0)
    ws.write(0, 2, 'Организация', style0)
    ws.write(0, 3, 'Должность', style0)
    ws.write(0, 4, 'Контактные данные', style0)
    ws.write(0, 5, 'Контактные данные', style0)
    ws.write(0, 6, 'Контактные данные', style0)
    ws.write(0, 7, 'Контактные данные', style0)
    ws.write(0, 8, 'Контактные данные', style0)
    ws.write(0, 9, 'Контактные данные', style0)
    ws.write(0, 10, 'Контактные данные', style0)
    ws.write(0, 11, 'Контактные данные', style0)
    ws.write(0, 12, 'Контактные данные', style0)

    ws.write(1, 0, arr[0], style1)
    ws.write(1, 1, arr[1], style1)
    ws.write(1, 2, arr[2], style1)
    ws.write(1, 3, arr[3], style1)
    ws.write(1, 4, arr[4], style1)
    ws.write(1, 5, arr[5], style1)
    ws.write(1, 6, arr[6], style1)
    ws.write(1, 7, arr[7], style1)
    ws.write(1, 8, arr[8], style1)
    ws.write(1, 9, arr[9], style1)
    ws.write(1, 10, arr[10], style1)
    ws.write(1, 11, arr[11], style1)
    ws.write(1, 12, arr[12], style1)

    wb.save('example.xls')
