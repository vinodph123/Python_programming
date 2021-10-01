import unittest

## In this file, setUpClass() and tearDownClass() are used as class fuxtures
## These method will be called once only unlike other setup and teardown methods 

class Temp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('This is setup class method added in class')

    @classmethod
    def tearDownClass(self):
        print('This is tearDown class method to test the tear down class')

    def setUp(self):
        global a
        a = open('test.txt','r+')


    def tearDown(self):
        a.close()    

    def test_write(self):
        a.writelines(input('Please enter the data to be added to file = '))

    def test_read(self):
        print(a.readlines())

    def test_check(self):
        print('This is to check whether class setup and teardown functions will work ')

if __name__ == '__main__':
    unittest.main()
