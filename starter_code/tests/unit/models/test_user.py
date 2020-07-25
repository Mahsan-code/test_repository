from starter_code.models.user import  UserModel
from unittest import TestCase

class UserTest(TestCase):

    def test_create_user(self):

        user = UserModel('mahsan', 'm1234')

        self.assertEqual(user.username, 'mahsan')
        self.assertEqual(user.password,'m1234')

