import unittest
from app import app, init_app

post_param = {
    "name": "my very First Session",
    "category": {
        "value": "fitness",
        "uuid": "f0c9011b-ff53-4cad-a747-2233fb343661"
    },
    "hashtags": [
        "#bestof2021", "#fitIndia", "#unittest"
    ],
    "description": {
        "value": "Unit test in 2021",
        "code": "en"
    },
    "creator_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "tokens": 0
}

put_param = {
    "sessionUUID": "8bff1e86-890d-49f7-9b72-b41c75ef440a",
    "name": "First Session",
    "category": {
        "value": "fitness",
        "uuid": "f0c9011b-ff53-4cad-a747-2233fb343661"
    },
    "hashtags": [
        "#bestof2021", "#fitIndia", "#unittest"
    ],
    "description": {
        "value": "Unit test module for put",
        "code": "en"
    },
    "creator_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "tokens": 0
}


class TestCreateSuccess(unittest.TestCase):

    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def test_get(self):
        response = self.app.get('/api/v1/sessions/')
        self.assertEqual(response.status_code, 200)

    # def test_post(self):
    #     response = self.app.post('/api/v1/sessions/', json=post_param)
    #     self.assertEqual(response.status_code, 201)
    #
    # def test_put(self):
    #     response = self.app.put('/api/v1/sessions/', json=put_param)
    #     self.assertEqual(response.status_code, 202)
    #
    # def test_delete(self):
    #     response = self.app.delete('api/v1/sessions/?session_uuid=9be0a2e8-303c-4fb9-bebf-b4c06a809339')
    #     self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
