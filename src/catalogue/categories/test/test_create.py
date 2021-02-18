import unittest
from app import app, init_app


class TestCreateSuccess(unittest.TestCase):

    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get(self):
        rv = self.app.get('/api/v1/categories/?language=en')
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
