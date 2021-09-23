class CellPhone:
    
    def __init__(self, m, n, rp):
        self.__manufact = m
        self.__model = n
        self.__price = rp

    def set_manufact(self, m):
        self.__manufact = m

    def set_model(self, n):
        self.__model = n


    def set_retail_price(self, rp):
        self.__price = rp

    def return_manufact(self):
        return self.__manufact

    def return_model(self):
        return self.__model

    def return_retail_price(self):
        return self.__price

    

    

