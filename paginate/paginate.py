class Paginate(object):
    def __init__(self, itens: list, step = 5):
        self.__itens = itens
        self.__step = step
        self.__init_page = 0
        self.__end_page = self.__init_page + self.__step
        self.__len = len(itens)

    def get_page(self):
        return self.__itens[self.__init_page:self.__end_page]

    def next_page(self):
        if (self.has_next()):
            self.__init_page = self.__end_page
            self.__end_page = self.__end_page + self.__step
        
    def prev_page(self):
        if (self.has_prev()):
            self.__end_page = self.__init_page
            self.__init_page = self.__init_page - self.__step

    def has_next(self):
        return self.__init_page + self.__step < self.__len
        
    def has_prev(self):
        return self.__init_page - self.__step >= 0