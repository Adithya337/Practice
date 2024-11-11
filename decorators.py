# Return a Function as a Value
'''
def greeting(name):
    def hello():
        return f'My name is {name}'
    return hello


a = greeting('Adithya')
print(a())
'''
# Passing function as a argument
'''
def main_func(func, a, b):
    return func(a, b)

def func(a, b):
    return a+b

a = main_func(func, 10, 20)
print(a)

'''

# smart Divide

'''
def smart_divide(func):
    def inner(a, b):
        print("I am inside inner function")
        if b == 0:
            print(f'b is not correct value')
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a+b)


divide(10, 5)
'''


class Person:
    __name = None
    __salary = None

    def __init__(self):
        self.__name = 'Adithya'
        self.__salary = 78000
    # salary = 7800

    @property
    def show(self):
        return self.__salary, self.__name

    @show.setter
    def show(self, name1):
        self.__name = name1


a = Person()
print(a.show)
a.show = 'Surya'
print(a.show)
# print(dir(a))
