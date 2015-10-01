from tests.base import BaseTest
import flask
import run
import unittest

class FormTestCase(BaseTest):
    def test_submit_with_errors(self):
        recorded = []

        def record(sender, message, category):
            recorded.append((message, category))

        flask.message_flashed.connect(record, run.app)

        with self.client.post('/') as r:
            self.assertTrue(len(recorded) > 0)

if __name__ == '__main__':
    unittest.main()
