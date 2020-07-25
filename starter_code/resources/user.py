from  flask_restful import  Resource, reqparse

from starter_code.models.user import UserModel


class UserRegister(Resource):

    """
    this resource allows us to register by sending a POST request with thier
    username and pasword
    """

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type = str,
                        required= True,
                        help= 'this filed can not be blank')

    parser.add_argument('password',
                        type=str,
                        required = True,
                        help= 'filed can not be blank')

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'user already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'user created successfully'}, 201
