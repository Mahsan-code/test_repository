from   starter_code.models.user import UserModel
from starter_code.tests.base_test import BaseTest
import  json
from  flask.testing import FlaskClient


class UserTest(BaseTest):

    def test_register_user(self):
        with self.app() as client:
            with self.app_context():

                request = client.post('/register', data ={'username': 'mahsan', 'password': 'mah1234'})
                self.assertEqual(request.satus_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('mahsan'))
                self.assertDictEqual({'message':'user created successfully'},
                                     json.loads(request.data))


    def test_register_login(self):
        with self.app() as client:
            with self.app_context():

                request = client.post('/register', data ={'username': 'mahsan', 'password': 'mah1234'})
                auth_respond = client.post('/auth',
                                           data = json.dumps({'username': 'mahsan', 'password':'mah1234'}),
                                           header = {'content_type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_respond.data).keys())


    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'mahsan', 'password': 'mah1234'})
                respond = client.post('/register', data={'username': 'mahsan', 'password': 'mah1234'})

                self.assertEqual(respond.status_code, 400)
                self.assertDictEqual({'message': 'a user with username already exists'},
                                     json.loads(respond.data))