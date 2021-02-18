import unittest
from app import app, init_app

post_param = {
    "ref_uuid": "1384b093-9c2f-47e7-9829-f931efc5d82c",
    "max_slots": "100"
}


class TestCreateSuccess(unittest.TestCase):

    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def test_get(self):
        rv = self.app.get('/api/v1/availabilities/2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9')
        self.assertEqual(rv.status_code, 200)

    def test_post(self):
        rv = self.app.post('/api/v1/availabilities/', json=post_param)
        self.assertEqual(rv.status_code, 201)

    def test_patch_decrease(self):
        rv = self.app.patch('/api/v1/availabilities/43906fc2-279f-4be1-a866-c7393b689b99/decrease')
        self.assertEqual(rv.status_code, 200)

    def test_patch_increase(self):
        rv = self.app.patch('/api/v1/availabilities/43906fc2-279f-4be1-a866-c7393b689b99/increase')
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
