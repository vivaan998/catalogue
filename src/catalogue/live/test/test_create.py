import unittest
from app import app, init_app

post_params = {
    "live": {
        "from": "2021-01-17 18:25:14.83",
        "to": "2021-01-17 21:25:14.83",
        "presenter_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "description": "Live Unit Test",
        "hashtags": ["unit", "test"],
        "language": "en"
    },
    "session_uuid": "917de83e-1825-4bbb-bd58-3fb1a8959bfd"
}

put_params = {
    "live": {
        "from": "2021-03-17 18:25:14.83",
        "to": "2021-03-17 21:25:14.83",
        "presenter_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "description": "Unit Test",
        "hashtags": ["working", "#updated"],
        "language": "en"
    },
    "liveUUID": "c1e49034-3a74-4f02-b896-a4d0b2b8f215",
    "session_uuid": "917de83e-1825-4bbb-bd58-3fb1a8959bfd"
}


class TestCreateSuccess(unittest.TestCase):

    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def test_get(self):
        response = self.app.get('/api/v1/lives/?live_uuid=2bd7b9a9-d0a4-4967-bba0-4d1c79c3cbe9')
        self.assertEqual(response.status_code, 200)

    def test_get_all_lives(self):
        response = self.app.get('/api/v1/lives/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.app.post('/api/v1/lives/', json=post_params)
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        response = self.app.put('/api/v1/lives/', json=put_params)
        self.assertEqual(response.status_code, 202)

    def test_delete(self):
        response = self.app.delete('/api/v1/lives/?live_uuid=80f9f1e8-77a8-40ae-bfe8-e3c1ee0fade7')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
