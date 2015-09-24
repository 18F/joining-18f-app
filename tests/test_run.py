import run
import unittest

class Joining18FAppTestCase(unittest.TestCase):
    def setUp(self):
        run.app.testing = True
        self.app = run.app.test_client()

    def test_apply(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertRegexpMatches(str(r.data), r'\<form.*')

if __name__ == '__main__':
    unittest.main()
