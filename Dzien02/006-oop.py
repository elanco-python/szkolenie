
# OOP

class MetaProduct:
    pass

class Product:

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_info(self):
        return f"ID={self.__id}, name={self.__name}, price={self.__price}"

    def __str__(self):
        #return f"ID={self.__id}, name={self.__name}, price={self.__price}"
        return self.get_info()

    def set_price(self, new_price):
        self.__price = new_price

cola_cola = Product(1, "Coca-Cola", 4.99)
print(cola_cola.get_info())
cola_cola.set_price(3.99)
print(cola_cola.get_info())
cola_cola._Product__price = 123
print(cola_cola.get_info())
print("="*60)
print(cola_cola)
#print(dir(cola_cola))