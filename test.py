# from openpyxl import Workbook, load_workbook
# from openpyxl.utils.dataframe import dataframe_to_rows
# import pandas as pd 
# import os

# # path = os.getcwd()
# # new_path = path +
# arr = [123, 31, 321]
# # print(path)
# if os.path.exists(r'.\sample.xlsx') == True:
#     # list of strings

#     # Calling DataFrame constructor on list
#     # df = pd.DataFrame(arr)

#     wb = load_workbook('sample.xlsx')
#     ws = wb.active

#     # for r in dataframe_to_rows(df, index=True, header=True):
#     ws.append(arr)

#     wb.save('sample.xlsx')
# else:
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['Имя', 'Фамилия', 'Организация', 'Должность', 'Контактные данные', 'Уровень влияния', 'Заинтересованность', 'Нужды и потребности', 'Ожидания', 'Уровень заинтересованности', 'Эффект на ПМ', 'Проблематичность', 'Коммуникативность', 'Советы'])
#     ws.append(arr)
#     wb.save("sample.xlsx")

# os