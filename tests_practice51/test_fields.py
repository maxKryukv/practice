import unittest

from flask import request

from practice51 import app, registration


class TestFields(unittest.TestCase):
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_email(
            self,
            email=None,
            phone=99912345671,
            name='Иванов иван',
            index=187110,
            comment='вход со двора'
    ):
        response = self.app.post(self.base_url, data=dict(
            email=email,
            phone=phone,
            name=name,
            index=index,
            comment=comment
        ))
        response_text = response.data.decode()
        expectation = "Invalid email", 400
        self.assertEqual(response_text, expectation)


if __name__ == '__main__':
    unittest.main()
