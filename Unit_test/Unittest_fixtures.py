import unittest

## This is basic unittest package practice
## Fixtures are added here like We can add setUP() for configuring fixture and teardown()
## for destroying the configuration
## Each function and class has to be named with Test so that unittest case execute

class Testmac(unittest.TestCase):

    global a 
    global b
    a = 30
    b = 30

    def setUp(self):
        print('Configuration set up completed')

    def tearDown(self):
        print('Tear down done ....!')

    def test_validate(self):
        self.assertEqual(a,b)

    def test_fun(self):
        self.assertNotRegex('vinod hulagabali','vishnu')

    def test_sample(self):
        #('sample tested')
        pass

    def test_simple(self):
        #print('simple tested')
        pass
        


if __name__ == '__main__':
    unittest.main()
        
        