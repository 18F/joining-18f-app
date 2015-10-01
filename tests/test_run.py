from tests.base import BaseTest
import unittest

class Joining18FAppTestCase(BaseTest):
    def test_apply(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertRegexpMatches(str(r.data), r'\<form.*')

if __name__ == '__main__':
    unittest.main()
