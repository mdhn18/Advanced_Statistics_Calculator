
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
        response_data = self.app.get('/max?X=1,2,5,0,100'')
        self.assertEqual(b'100.0\n', response_data.data)

    def test_mean(self):
        response_data = self.app.get('/mean?X=1,2,5,0,100')
        self.assertEqual(b'21.6\n', response_data.data)

    def test_mean(self):
        response_data = self.app.get('/mean?X=1000,2.5,100')
        self.assertEqual(b'367.5\n', response_data.data)

    def test_avg(self):
        response_data = self.app.get('/avg?X=1,2,5,0,100')
        self.assertEqual(b'21.6\n', response_data.data)

    def test_average(self):
        response_data = self.app.get('/average?X=1,2,5,0,100')
        self.assertEqual(b'21.6\n', response_data.data)

    def test_min(self):
        response_data = self.app.get('/min?X=1,4,9,0,50')
        self.assertEqual(b'1.0\n', response_data.data)

    def test_min(self):
        response_data = self.app.get('/min?X=1,2,5,0,100,-100,-5,-2')
        self.assertEqual(b'-100.0\n', response_data.data)

    def test_median(self):
        response_data = self.app.get('/median?X=1,2,5,0,100,-100,-5,-2')
        self.assertEqual(b'0.5\n', response_data.data)

    def test_median(self):
        response_data = self.app.get('/median?X=4,5,56,78')
        self.assertEqual(b'0.5\n', response_data.data)
if __name__ == '__main__':
    unittest.main()
    