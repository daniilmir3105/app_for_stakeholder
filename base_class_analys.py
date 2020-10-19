from abc import ABCMeta, abstractmethod

class base_analys_of_parametr(metaclass=ABCMeta):
    '''
    This metaclass will have merhods
    '''

    # 
    # __parametr = 0

    # this will be base-method for getting the vallue of parametr  
    @abstractmethod
    def make_analys(self):
        pass

class impact_level(base_analys_of_parametr):
    '''
    In this class will be our method for analys of impact from stakeholder 
    '''

    __parametr_1 = 0

    def make_analys(self, impact_level) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of impact on the project
        '''
        
        self.__parametr_1 = 2 if impact_level == 'высокий' else -2 if impact_level == 'низкий' else 0
        return self.__parametr_1

class engagement(base_analys_of_parametr):
    '''
    In this class will be our method for analys of engagement from stakeholder
    '''

    __parametr_2 = 0

    def make_analys(self, engagement_rate) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of engagement of stakeholder
        '''
        
        self.__parametr_2 = 2 if engagement_rate == 'вовлеченность' else 1 if engagement_rate == 'лояльность' else -1 if engagement_rate == 'нелояльность' else -2 if engagement_rate == 'вредительство' else 0
        return self.__parametr_2

class needs_and_requirements(base_analys_of_parametr):
    '''
    In this class will be our method for analys of needs and requirements from stakeholder
    '''

    __parametr_3 = 0 

    def make_analys(self, needs_requirements) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of needs and requirements of stakeholder
        '''

        self.__parametr_3 = 2 if needs_requirements == 'прибыль' else 1 if needs_requirements == 'паблисити' else -2 if needs_requirements == 'провал проекта' else 0
        return self.__parametr_3

class expectations(base_analys_of_parametr):
    '''
    In this class will be our method for analys of expectations of stakeholder
    '''

    __parametr_4 = 0

    def make_analys(self, expectations) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of expectations about project from stakeholder
        '''

        self.__parametr_4 = 2 if expectations == 'успех' else -2 if expectations == 'неудача' else 0
        return self.__parametr_4

class level_of_interests(base_analys_of_parametr):
    '''
    In this class will be our method for analys of level of interests of stakeholder
    '''

    __parametr_5 = 0

    def make_analys(self, level_and_quality_of_interest) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of level of interests of stakeholder
        '''

        self.__parametr_5 = 2 if level_and_quality_of_interest == 'союзники' else 1 if level_and_quality_of_interest == 'поддерживающие' else -1 if level_and_quality_of_interest == 'неохотно участвующие' else -2 if level_and_quality_of_interest == 'оппоненты' else 0
        return self.__parametr_5

class effect(base_analys_of_parametr):
    '''
    In this class will be our method for analys of effect on project manager of stakeholder
    '''

    __parametr_6 = 0

    def make_analys(self, effect_of_a_pm_on_a_stakeholder) -> base_analys_of_parametr:
        '''
        This is a method, that will score parametr of level of effect on project manager of stakeholder
        '''

        self.__parametr_6 = 2 if effect_of_a_pm_on_a_stakeholder == 'высокий' else 1 if effect_of_a_pm_on_a_stakeholder == 'средний' else -2 if effect_of_a_pm_on_a_stakeholder == 'низкий' else 0
        return self.__parametr_6

class problematical_character(base_analys_of_parametr):
    '''
    This class will show how problematic is a stakeholder
    '''

    __parametr_7 = 0

    def make_analys(self, problem) -> base_analys_of_parametr:
        '''
        This method will show how problematic is a stakeholder
        '''

        self.__parametr_7 = 2 if problem == 'безпроблемный' else -1 if problem == 'средне-проблематичный' else -2 if problem == 'проблематичный' else 0
        return self.__parametr_7

class communicativity(base_analys_of_parametr):
    '''
    This class will show how communicative is a stakeholder
    '''

    __parametr_8 = 0

    def make_analys(self, communicative) -> base_analys_of_parametr:
        '''
        This method will show how communicative is a stakeholder
        '''

        self.__parametr_8 = 2 if communicative == 'высокая' else -2 if communicative == 'низкая' else 0
        return self.__parametr_8
