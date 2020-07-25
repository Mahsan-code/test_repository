from starter_code.models.user import UserModel
from starter_code.tests.test_base import BaseTest
from starter_code.app import app

class UserTest (BaseTest):

    def test_crud(self):
        with app.app_context():
            user = UserModel('mahsan', 'm1234')

            self.assertIsNone(UserModel.find_by_username('mahsan'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()
            self.assertIsNotNone(UserModel.find_by_username('mahsan'))
            self.assertIsNotNone(UserModel.find_by_id(1))

