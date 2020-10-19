import hack_class
import numpy as np 
import start_vvod as s_v

how_many = s_v.inp()
N = how_many.question()

if __name__ == '__main__':
    for i in range(N):
        how_many.basic_inf()

        per_1 = input('Каков уровень влияния стейкхолдера на рабочий процесс?(высокий, средний, низкий)\nВспомогательные вопросы: «Как сильно проект повлияет на стейкхолдера? Насколько проект значим для него?»\nУровень влияния: ')
        per_2 = input('Насколько сильно этот стейкхолдер может повлиять на проект? Дополнительно: каким может быть его вклад – что это за ресурсы или действия? Как много и часто он может вложить свои ресурсы в проект?\nВовлеченность сотрудника(вовлеченность, лояльность, нейтралитет, нелояльность, вредительство): ')
        per_3 = input('Что важно и нужно этому стейкхолдеру?\nНапример: прибыль, паблисити, ничего, провал проекта.\nПотребности стейкхолдера: ')
        per_4 = input('Каких конкретных результатов ожидает стейкхолдер(успех, никаких ожиданий, неудача)?: ')
        per_5 = input('К какому кругу относится стейкхолдер (союзники, поддерживающие, нейтральные, неохотно участвующие, оппоненты): ')
        per_6 = input('Влияние проектного менеджера на стейкхолдера (высокий - для подчиненных; средний - для начальства; низкий - для человека вне организации): ')
        per_7 = input('На сколько проблематичен стейкхолдер(безпроблемный, средне-проблематичный, проблематичный)?: ')
        per_8 = input('На каком уровне находится коммуникативность индивида(высокая, средняя, низкая)?: ')

        #h_vvod = s_v.vvod()
        #h_vvod.frage(N, vorname, nachname, organisation, position, contacts)

        h_as = hack_class.analys()

        param_1 = h_as.impact(per_1)
        param_2 = h_as.engagement(per_2)
        param_3 = h_as.needs(per_3)
        param_4 = h_as.expectations_from_stakeholder(per_4)
        param_5 = h_as.level(per_5)
        param_6 = h_as.effect(per_6)
        param_7 = h_as.problematic(per_7)
        param_8 = h_as.communicativity(per_8)

        scoring_result_1 = h_as.scoring_1(param_1, param_2, param_7, param_8)
        scoring_result_2 = h_as.scoring_2(param_3, param_4, param_5, param_6, )

        # h_an = hack_class.analys()
        h_as.anal(scoring_result_1, scoring_result_2)

        # x = np.arange[]