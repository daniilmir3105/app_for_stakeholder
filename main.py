import base_class_analys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from interface_2 import Ui_Dialog
import base_class_analys
import become_result

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

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

class Stakeholder(QtWidgets.QMainWindow, Ui_Dialog):
    '''
    This class will have all fields and methods for stakeholder analys
    '''

    def __init__(self):
        '''
        Construktor of our class
        '''
        super().__init__()

        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)

        # Показать наше окно
        self.show()

        self.pushButton.clicked.connect(self.digit_pressed)

    def digit_pressed(self):
        '''
        Method, thar return some data of person
        '''

        # personal data
        name_line = ui.lineEdit.text()
        family_name_line = ui.lineEdit_2.text()
        organisation_name_line = ui.lineEdit_3.text()   
        position_line = ui.lineEdit_4.text()
        contacts_line = ui.lineEdit_5.text()

        # data that we become from comboboxes(our main-parametrs for analys)
        param_1 = ui.comboBox.currentText()
        param_2 = ui.comboBox_2.currentText()
        param_3 = ui.comboBox_3.currentText()
        param_4 = ui.comboBox_4.currentText()
        param_5 = ui.comboBox_5.currentText()
        param_6 = ui.comboBox_6.currentText()
        param_7 = ui.comboBox_7.currentText()
        param_8 = ui.comboBox_8.currentText()

        result = []
        result.append(name_line)
        result.append(family_name_line)
        result.append(organisation_name_line)
        result.append(position_line)
        result.append(contacts_line)
        result.append(param_1)
        result.append(param_2)
        result.append(param_3)
        result.append(param_4)
        result.append(param_5)
        result.append(param_6)
        result.append(param_7)
        result.append(param_8)

        return result
        
def making_analys(result_param):
    '''
    This function will make analys and get the result 
    '''
    # score result of parametrs 
    g_1 = analys_param_1.make_analys(result_param[5])
    g_2 = analys_param_2.make_analys(result_param[6])
    g_3 = analys_param_3.make_analys(result_param[7])
    g_4 = analys_param_4.make_analys(result_param[8])
    g_5 = analys_param_5.make_analys(result_param[9])
    g_6 = analys_param_6.make_analys(result_param[10])
    g_7 = analys_param_7.make_analys(result_param[11])
    g_8 = analys_param_8.make_analys(result_param[12])

    # final result for matrix of stakeholder
    result_x = final_result.scoring_1(g_1=g_1, g_2=g_2, g_7=g_7, g_8=g_8)
    result_y = final_result.scoring_2(g_3=g_3, g_4=g_4, g_5=g_5, g_6=g_6)

    # what to do with this person
    final = final_result.make_simple_analys(x=result_x, y=result_y)
    return final

def launchApp(app):
    appController = ApplicationController()
    appController.showMainWindow()
    return app.exec_()

if __name__ == "__main__":
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    
    # Сoздание инстанса класса , который мы создадим далее
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()

    result = launchApp(app=app)

    stakeholder = Stakeholder()

    sys.exit(result)
