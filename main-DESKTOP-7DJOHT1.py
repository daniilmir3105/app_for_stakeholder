import base_class_analys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from interface_2 import Ui_Dialog
import base_class_analys
import become_result
import os
import xlwt

# making objects for analys
analys_param_1 = base_class_analys.impact_level()
analys_param_2 = base_class_analys.engagement()
analys_param_3 = base_class_analys.needs_and_requirements()
analys_param_4 = base_class_analys.expectations()
analys_param_5 = base_class_analys.level_of_interests()
analys_param_6 = base_class_analys.effect()
analys_param_7 = base_class_analys.problematical_character()
analys_param_8 = base_class_analys.communicativity()

# making object to become a result 
final_result = become_result.result()

# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()

class Stakeholder(QtWidgets.QMainWindow, Ui_Dialog):
    '''
    This class will have all fields and methods for stakeholder analys
    '''

    __result = []

    def __init__(self):
        '''
        Construktor of our class
        '''
        super().__init__()

        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)

        # Показать наше окно
        self.show()

        self.pushButton.clicked.connect(self.making_analys)

    def get_data(self):
        '''
        Method, thar return some data of person
        '''

        return self.__result
        
    def making_analys(self):
        '''
        This function will make analys and get the result 
        '''
        # score result of parametrs 
        name_line = self.lineEdit.text()
        family_name_line = self.lineEdit_2.text()
        organisation_name_line = self.lineEdit_3.text()   
        position_line = self.lineEdit_4.text()
        contacts_line = self.lineEdit_5.text()

        # data that we become from comboboxes(our main-parametrs for analys)
        param_1 = self.comboBox.currentText()
        param_2 = self.comboBox_2.currentText()
        param_3 = self.comboBox_3.currentText()
        param_4 = self.comboBox_4.currentText()
        param_5 = self.comboBox_5.currentText()
        param_6 = self.comboBox_6.currentText()
        param_7 = self.comboBox_7.currentText()
        param_8 = self.comboBox_8.currentText()

        self.__result.append(name_line)
        self.__result.append(family_name_line)
        self.__result.append(organisation_name_line)
        self.__result.append(position_line)
        self.__result.append(contacts_line)
        self.__result.append(param_1)
        self.__result.append(param_2)
        self.__result.append(param_3)
        self.__result.append(param_4)
        self.__result.append(param_5)
        self.__result.append(param_6)
        self.__result.append(param_7)
        self.__result.append(param_8)
        g_1 = analys_param_1.make_analys(self.__result[5])
        g_2 = analys_param_2.make_analys(self.__result[6])
        g_3 = analys_param_3.make_analys(self.__result[7])
        g_4 = analys_param_4.make_analys(self.__result[8])
        g_5 = analys_param_5.make_analys(self.__result[9])
        g_6 = analys_param_6.make_analys(self.__result[10])
        g_7 = analys_param_7.make_analys(self.__result[11])
        g_8 = analys_param_8.make_analys(self.__result[12])

        # final result for matrix of stakeholder
        result_x = final_result.scoring_1(g_1=g_1, g_2=g_2, g_7=g_7, g_8=g_8)
        result_y = final_result.scoring_2(g_3=g_3, g_4=g_4, g_5=g_5, g_6=g_6)

        # what to do with this person
        final = final_result.make_simple_analys(x=result_x, y=result_y)

        if final == 'Данная личность не является стейкхолдером.':
            final_data = os.startfile(r'C:\Users\lenovo\OneDrive - Peter the Great St. Petersburg Polytechnical University\Документы\Daniil\programming\python\projects\app_for_stakeholder\not.png')
        elif final == 'Данный стейкхолдер относится к блоку «Хорошие отношения»:\nC этими стейкхолдерами необходимо установить тесные рабочие отношения, потому что для них проект важен, они вовлечены в реализацию и активно влияют на процесс и результат.':
            final_data = os.startfile(r'C:\Users\lenovo\OneDrive - Peter the Great St. Petersburg Polytechnical University\Документы\Daniil\programming\python\projects\app_for_stakeholder\good_relation.png')
        elif final == 'Данный стейкхолдер относится к блоку «Мониторинг»:\nОни имеют власть над реализацией проекта, но не слишком заинтересованы в нем.\nПри таком сочетании факторов они могут стать источниками рисков, поэтому необходимы тщательный мониторинг и внимательный менеджмент.':
            final_data = os.startfile(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\monitor.png')
        elif final == 'Данный стейкхолдер относится к блоку «Низкий приоритет»: этот стейкхолдер вовлечен и относительно заинтересован, но от него зависит не так много, поэтому с точки зрения распределения менеджерского внимания, у него низкий приоритет.':
            final_data = os.startfile(r'C:\Users\lenovo\OneDrive - Peter the Great St. Petersburg Polytechnical University\Документы\Daniil\programming\python\projects\app_for_stakeholder\low_priority.png')
        else: 
            final_data = os.startfile(r'C:\Users\lenovo\OneDrive - Peter the Great St. Petersburg Polytechnical University\Документы\Daniil\programming\python\projects\app_for_stakeholder\protect.png')
    
        if True:
            pass
        else:
            font0 = xlwt.Font()
            font0.name = 'Times New Roman'
            font0.colour_index = xlwt.Style.colour_map['black']
            font0.bold = True

            font1 = xlwt.Font()
            font1.name = 'Times New Roman'
            font1.colour_index = xlwt.Style.colour_map['black']
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
            ws.write(0, 13, 'Рекомендации', style0)

            ws.write(1, 0, self.__result[0], style1)
            ws.write(1, 1, self.__result[1], style1)
            ws.write(1, 2, self.__result[2], style1)
            ws.write(1, 3, self.__result[3], style1)
            ws.write(1, 4, self.__result[4], style1)
            ws.write(1, 5, self.__result[5], style1)
            ws.write(1, 6, self.__result[6], style1)
            ws.write(1, 7, self.__result[7], style1)
            ws.write(1, 8, self.__result[8], style1)
            ws.write(1, 9, self.__result[9], style1)
            ws.write(1, 10, self.__result[10], style1)
            ws.write(1, 11, self.__result[11], style1)
            ws.write(1, 12, self.__result[12], style1)
            ws.write(1, 13, final, style1)

            wb.save('example.xls')

        return final_data

if __name__ == "__main__":
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    
    # Сoздание инстанса класса, который мы создадим далее
    stakeholder = Stakeholder()
    # stakeholder.get_data()
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    
    sys.exit(app.exec_())
