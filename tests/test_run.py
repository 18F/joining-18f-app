import run
import unittest

class Joining18FAppTestCase(unittest.TestCase):
    def setUp(self):
        run.app.config['TESTING'] = True
        self.app = run.app.test_client()

    def test_apply(self):
        response = self.app.get('/')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Apply to 18F!")

if __name__ == '__main__':
    unittest.main()
