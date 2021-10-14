# Decorator practice 

class Sample:

    def __init__(self):
        pass

    def dec(self,test):

        def wrap_function():
            print('Before the decorator called ')
            test()
            print('After the decorator called')
        return wrap_function


def fun_needed_to_be_decorated():
    print('Function decorated')

if __name__ == '__main__':
    s = Sample()
    d = s.dec(fun_needed_to_be_decorated)
    d()