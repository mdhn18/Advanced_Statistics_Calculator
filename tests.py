
import unittest
import main



class TestOnlineCalculator(unittest.TestCase):
    """Testing features of online calculator"""

    def setUp(self):
        """Sets up the app for testing"""

        main.app.testing = True
        self.app = main.app.test_client() 

    def test_empty_page(self):
        """ Tests the page with no route"""
        response_data = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?X=<Value1, value2, value2, .... , valueN>\n', response_data.data)

        # Testing POST Method
        response_data = self.app.post('/')
        self.assertEqual(b'Usage;\n<Operation>?X=<Value1, value2, value2, .... , valueN>\n', response_data.data)
        
    def test_max(self):
        response_data = self.app.get('/max?X=4,5,56,78')
        self.assertEqual(b'78.0\n', response_data.data)

    def test_max(self):
        response_data = self.app.get('/max?X=1,2,5,0,100')
        self.assertEqual(b'100.0\n', response_data.data)

if __name__ == '__main__':
    unittest.main()
    