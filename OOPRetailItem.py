class RetailItem:


    def __init__(self, description, units_inventory, price):
        self.__descrip = description
        self.__units = units_inventory
        self.__retailprice = price


    #def set__descrip(self, description):
     #   self.__descrip = description

    #def set__units_inventory(self, units_inventory):
     #   self.__units = units_inventory

    #def set__price(self, price):
     #   self.__retailprice = price

    def get_descrip(self):
        return self.__descrip

    def get_units_inventory(self):
        return self.__units

    def get_price(self):
        return self.__retailprice




    