# from abc import ABC, abstractmethod

class result:
    '''
    Class, that makes mathematic operations for become a result:
    '''

    def scoring_1(self, g_1, g_2, g_7, g_8):
        ''' Score the results. '''
        
        x = g_8 + g_2 + g_1 + g_7

        return x

    def scoring_2(self, g_3, g_4, g_5, g_6):
        ''' Score the results. '''

        y = g_3 + g_4 + g_5 + g_6

        return y

    def make_simple_analys(self, x, y):
        ''' Making simple analys for stakeholder '''

        if x == 0 and y == 0:
            result = 'Данная личность не является стейкхолдером.'
            f = open(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\not.png')
            input()
            f.close()
            return result
        elif x > 0 and y > 0:
            result = 'Данный стейкхолдер относится к блоку «Хорошие отношения»:\nC этими стейкхолдерами необходимо установить тесные рабочие отношения, потому что для них проект важен, они вовлечены в реализацию и активно влияют на процесс и результат.'
            f = open(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\good_relation.png')
            input()
            f.close()
            return result
        elif x > 0 and y < 0:
            result = 'Данный стейкхолдер относится к блоку «Мониторинг»:\nЗдесь на карту нанесены стейкхолдеры, которые имеют власть над реализацией проекта, но не слишком заинтересованы в нем.\nПри таком сочетании факторов они могут стать источниками рисков, поэтому тут требуются тщательный мониторинг и внимательный менеджмент.'
            f = open(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\monitor.png')
            input()
            f.close()
            return result
        elif x < 0 and y < 0:
            result = 'Данный стейкхолдер относится к блоку «Низкий приоритет»: этот стейкхолдер вовлечен и относительно заинтересован, но от него зависит не так много, поэтому с точки зрения распределения менеджерского внимания, у него низкий приоритет.'
            f = open(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\low_priority.png')
            input()
            f.close()
            return result
        else:
            result = 'Данный стейкхолдер относится к блоку «Защита»: тут на карте отмечены стейкхолдеры, для которых требуются специальные инициативы по защите их интересов, потому что для них проект достаточно важен, а их влияние на его реализацию незначительно (либо они вообще не имеют возможности повлиять).'
            f = open(r'C:\Users\lenovo\Documents\Daniil\programming\python\projects\app_for_stakeholder\protect.png')
            input()
            f.close()
            return result
