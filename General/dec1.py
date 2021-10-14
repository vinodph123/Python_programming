# Decorator concept practice

class Testing_decorator:

    def __init__(self) -> None:
        pass


    def decorator(self,fun):
        
        def dec():
            print('Before function to be decorated')
            fun()
            print('After the function decorated')
        return dec

def dec_fun():
    print('Function decorated')

def test_dec(test):

    def wrap():
        print('Before ')
        test()
        print('wawaawaawawaaaaaaaaaaaa/...!')
    return wrap

@test_dec
def test_direct():
    print('Testing direct method of decorating of the function')

if __name__ == '__main__':
    t = Testing_decorator() # Using class and method as decorator
    s = t.decorator(dec_fun)
    s()
    test_direct()