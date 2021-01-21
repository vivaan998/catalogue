import unittest
from app import app, init_app


class TestCreateSuccess(unittest.TestCase):

    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def test_get(self):
        rv = self.app.get('/api/v1/availabilities/')
        self.assertEqual(rv.status_code, 200)

    def test_post(self):
        rv = self.app.post('/api/v1/availabilities/', json={})
        self.assertEqual(rv.status_code, 200)

    def test_put(self):
        rv = self.app.put('/api/v1/availabilities/', json={})
        self.assertEqual(rv.status_code, 200)

    def test_delete(self):
        rv = self.app.delete('/api/v1/availabilities/')
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
