from abc import ABCMeta, abstractmethod

class assesment(metaclass=ABCMeta):
    ''' Create a new class for stakeholder assessment'''

    def impact(self, impact_level):
        ''' Assessment of the level of impact '''

        self.impact_level = impact_level

        if impact_level == 'высокий':
            g_1 = 2
        elif impact_level == 'средний':
            g_1 = 0
        elif impact_level == 'низкий':
            g_1 = -2
        else:
            print('Допустимые значения: высокий, средний, низкий.')
            impact_level = input(
                'Каков уровень влияния стейкхолдера на рабочий процесс?(высокий, средний, низкий)\nВспомогательные вопросы: «Как сильно проект повлияет на стейкхолдера? Насколько проект значим для него?»\nУровень влияния: ')
            if impact_level == 'высокий':
                g_1 = 2
            elif impact_level == 'средний':
                g_1 = 0
            elif impact_level == 'низкий':
                g_1 = -2
            else:
                g_1 = 0

        return g_1

    def engagement(self, engagement_rate):
        ''' The engagement rate on project. '''

        self.engagement_rate = engagement_rate

        if engagement_rate == 'вовлеченность':
            g_2 = 2
        elif engagement_rate == 'лояльность':
            g_2 = 1
        elif engagement_rate == 'нейтралитет':
            g_2 = 0
        elif engagement_rate == 'нелояльность':
            g_2 = -1
        elif engagement_rate == 'вредительство':
            g_2 = -2
        else:
            print('Допустимые значения: вовлеченность, лояльность, нейтралитет, нелояльность, вредительство.')
            engagement_rate = input('Насколько сильно этот стейкхолдер может повлиять на проект? Дополнительно: каким может быть его вклад – что это за ресурсы или действия? Как много и часто он может вложить свои ресурсы в проект?\nВовлеченность сотрудника(вовлеченность, лояльность, нейтралитет, нелояльность, вредительство): ')
            if engagement_rate == 'вовлеченность':
                g_2 = 2
            elif engagement_rate == 'лояльность':
                g_2 = 1
            elif engagement_rate == 'нейтралитет':
                g_2 = 0
            elif engagement_rate == 'нелояльность':
                g_2 = -1
            elif engagement_rate == 'вредительство':
                self.g_2 = -2
            else:
                g_2 = 0

        return g_2

    def needs(self, needs_requirements):
        ''' Needs and requirements from stakeholder. '''

        self.needs_requirements = needs_requirements

        if needs_requirements == 'прибыль':
            g_3 = 2
        elif needs_requirements == 'паблисити':
            g_3 = 1
        elif needs_requirements == 'ничего':
            g_3 = 0
        elif needs_requirements == 'провал проекта':
            g_3 = -2
        else:
            print('Допустимые значения: прибыль, паблисити, ничего, провал проекта.')
            needs_requirements = input(
                'Что важно и нужно этому стейкхолдеру?\nНапример: прибыль, паблисити, ничего, провал проекта.\nПотребности стейкхолдера: ')
            if needs_requirements == 'прибыль':
                g_3 = 2
            elif needs_requirements == 'паблисити':
                g_3 = 1
            elif needs_requirements == 'ничего':
                g_3 == 0
            elif needs_requirements == 'провал проекта':
                g_3 = -2
            else:
                g_3 = 0

        return g_3

    def expectations_from_stakeholder(self, expectations):
        ''' Engagement rate from stakeholder. '''

        self.expectations = expectations

        if expectations == 'успех':
            g_4 = 2
        elif expectations == 'никаких ожиданий':
            g_4 = 0
        elif expectations == 'неудача':
            g_4 = -2
        else:
            print('Допустимые значения: успех, никаких ожиданий, неудача')
            expectations = input(
                'Каких конкретных результатов ожидает стейкхолдер(успех, никаких ожиданий, неудача)?: ')
            if expectations == 'успех':
                g_4 = 2
            elif expectations == 'никаких ожиданий':
                g_4 = 0
            elif expectations == 'неудача':
                g_4 = -2
            else:
                g_4 = 0

        return g_4

    def level(self, level_and_quality_of_interest):
        ''' Level and quality of interests from stakeholder. '''

        self.level_and_quality_of_interest = level_and_quality_of_interest

        if level_and_quality_of_interest == 'союзники':
            g_5 = 2
        elif level_and_quality_of_interest == 'поддерживающие':
            g_5 = 1
        elif level_and_quality_of_interest == 'нейтральные':
            g_5 = 0
        elif level_and_quality_of_interest == 'неохотно участвующие':
            g_5 = -1
        elif level_and_quality_of_interest == 'оппоненты':
            g_5 = -2
        else:
            print('Допустимые значения: успех, никаких ожиданий, неудача.')
            level_and_quality_of_interest = input(
                'К какому кругу относится стейкхолдер (союзники, поддерживающие, нейтральные, неохотно участвующие, оппоненты): ')
            if level_and_quality_of_interest == 'союзники':
                g_5 = 2
            elif level_and_quality_of_interest == 'поддерживающие':
                g_5 = 1
            elif level_and_quality_of_interest == 'нейтральные':
                g_5 = 0
            elif level_and_quality_of_interest == 'неохотно участвующие':
                g_5 = -1
            elif level_and_quality_of_interest == 'оппоненты':
                g_5 = -2
            else:
                g_5 = 0

        return g_5

    def effect(self, effect_of_a_pm_on_a_stakeholder):
        ''' Effect of a project manager on stakeholder. '''

        self.effect_of_a_pm_on_a_stakeholder = effect_of_a_pm_on_a_stakeholder

        if effect_of_a_pm_on_a_stakeholder == 'высокий':
            g_6 = 2
        elif effect_of_a_pm_on_a_stakeholder == 'средний':
            g_6 = 1
        elif effect_of_a_pm_on_a_stakeholder == 'низкий':
            g_6 = -2
        else:
            print('Допустимые значения: высокий, средний, низкий.')
            effect_of_a_pm_on_a_stakeholder = input(
                'Влияние проектного менеджера на стейкхолдера (высокий - для подчиненных; средний - для начальства; низкий - для человека вне организации): ')
            if effect_of_a_pm_on_a_stakeholder == 'высокий':
                g_6 = 2
            elif effect_of_a_pm_on_a_stakeholder == 'средний':
                g_6 = 1
            elif effect_of_a_pm_on_a_stakeholder == 'низкий':
                g_6 = -2
            else:
                g_6 = 0

        return g_6

    def problematic(self, problem):
        ''' How problematic is a stakeholder. '''

        self.problem = problem

        if problem == 'безпроблемный':
            g_7 = 2
        elif problem == 'средне-проблематичный':
            g_7 = -1
        elif problem == 'проблематичный':
            g_7 = -2
        else:
            print('Допустимые значения: безпроблемный, средне-проблематичный, проблематичный.')
            problem = input(
                'На сколько проблематичен стейкхолдер(безпроблемный, средне-проблематичный, проблематичный)?: ')
            if problem == 'безпроблемный':
                g_7 = 2
            elif problem == 'средне-проблематичный':
                g_7 = -1
            elif problem == 'проблематичный':
                g_7 = -2
            else:
                g_7 = 0

        return g_7

    def communicativity(self, communicative):
        ''' How communicative is stakeholder. '''

        self.communicative = communicative

        if communicative == 'высокая':
            g_8 = 2
        elif communicative == 'средняя':
            g_8 = 0
        elif communicative == 'низкая':
            g_8 = -2
        else:
            print('Допустимые значения: высокая, средняя, низкая.')
            communicative = input('На каком уровне находится коммуникативность индивида(высокая, средняя, низкая)?: ')
            if communicative == 'высокая':
                g_8 = 2
            elif communicative == 'средняя':
                g_8 = 0
            elif communicative == 'низкая':
                g_8 = -2
            else:
                g_8 =0

        return g_8

    def scoring_1(self, g_1, g_2, g_7, g_8):
        ''' Score the results. '''
        
        x = g_8 + g_2 + g_1 + g_7

        return x

    def scoring_2(self, g_3, g_4, g_5, g_6):
        ''' Score the results. '''

        y = g_3 + g_4 + g_5 + g_6

        return y

class analys(assesment):
    ''' Here will be analys of scores of assesment. '''

    def anal(self, x, y):
        ''' Analys of scores. '''

        if x == 0 and y == 0:
            print('Данная личность не является стейкхолдером.')
        elif x >= 0 and y >= 0:
            print(
                'Данный стейкхолдер относится к блоку «Хорошие отношения»:\nC этими стейкхолдерами необходимо установить тесные рабочие отношения, потому что для них проект важен, они вовлечены в реализацию и активно влияют на процесс и результат.')
        elif x >= 0 and y < 0:
            print(
                'Данный стейкхолдер относится к блоку «Мониторинг»:\nЗдесь на карту нанесены стейкхолдеры, которые имеют власть над реализацией проекта, но не слишком заинтересованы в нем.\nПри таком сочетании факторов они могут стать источниками рисков, поэтому тут требуются тщательный мониторинг и внимательный менеджмент.')
        elif x < 0 and y < 0:
            print(
                'Данный стейкхолдер относится к блоку «Низкий приоритет»: этот стейкхолдер вовлечен и относительно заинтересован, но от него зависит не так много, поэтому с точки зрения распределения менеджерского внимания, у него низкий приоритет.')
        else:
            print(
                'Данный стейкхолдер относится к блоку «Защита»: тут на карте отмечены стейкхолдеры, для которых требуются специальные инициативы по защите их интересов, потому что для них проект достаточно важен, а их влияние на его реализацию незначительно (либо они вообще не имеют возможности повлиять).')
