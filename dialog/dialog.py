from paginate.paginate import Paginate

class Dialog(object):
    def __init__(self, telegram_id, age, auth):
        self.__ask = 0
        self.__state = 0
        self.__step = 0
        self.__movie = 0
        self.__dialog_id = 0
        self.__recommendation_id = 0
        self.__age = age
        self.__auth = auth
        self.__telegram_id = telegram_id
        self.__attributes = []
        self.__paginate = None

    # region Getters and Setters
    def __set_ask(self, ask: int = None):
        self.__ask = ask

    def __get_ask(self):
        return self.__ask

    def __set_auth(self, auth: int = None):
        self.__auth = auth

    def __get_auth(self):
        return self.__auth

    def __set_state(self, state: int = None):
        self.__state = state

    def __get_state(self):
        return self.__state

    def __set_step(self, step: int = None):
        self.__step = step

    def __get_step(self):
        return self.__step

    def __set_movie(self, movie: int = None):
        self.__movie = movie

    def __get_movie(self):
        return self.__movie

    def __set_dialog_id(self, dialog_id: int = None):
        self.__dialog_id = dialog_id

    def __get_dialog_id(self):
        return self.__dialog_id

    def __set_recommendation_id(self, recommendation_id: int = None):
        self.__recommendation_id = recommendation_id

    def __get_recommendation_id(self):
        return self.__recommendation_id

    def __set_attributes(self, attributes: int = None):
        self.__attributes = attributes

    def __get_attributes(self):
        return self.__attributes

    def __set_paginate(self, itens: list, step = 5):
        self.__paginate = Paginate(itens, step)

    def __get_paginate(self):
        return self.__paginate
    # endregion Getters and Setters

    # region Properties
    @property
    def age(self):
        return self.__age
    
    @property
    def telegram_id(self):
        return self.__telegram_id

    ask = property(__get_ask, __set_ask)

    auth = property(__get_auth, __set_auth)

    state = property(__get_state, __set_state)

    movie = property(__get_movie, __set_movie)

    dialog_id = property(__get_dialog_id, __set_dialog_id)

    recommendation_id = property(__get_recommendation_id, __set_recommendation_id)

    attributes = property(__get_attributes, __set_attributes)

    paginate = property(__get_paginate, __set_paginate)
    # endregion Properties