class Person :
    def __init__(self, name, age, address):
        self.__name =name
        self.age =age
        self.address =address

    def set_name(self, name):
        self.__name
    def get_name(self, name):
        self.__name = name
    def get_age(self, age):
        self.__age
    def set_age(self, age):
        self.__age= age
    def get_address(self, address):
        self.__address
    def set_address(self, address):
        self.__address= address
p = Person("mahum", 100,"Lahore")
print(p.get_name())
print(p.get_age())