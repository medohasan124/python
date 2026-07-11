
def my_decorator(func):
    def wapper():
        print("befor")
        func()
        print('after')
    return wapper



@my_decorator
def hello():
    print("hello boy")



hello()


