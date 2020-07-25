from werkzeug.security import safe_str_cmp
from starter_code.models.user import  UserModel


def authentication(username, password):
    """
    function that get called when a user calls the /auth endpoint
    with thier username and password
    :param username:user's username in str format
    :param password:user's un-encrypted password in str format
    :return:a usermodel object if authentication was successful
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return  user

def identity(payload):

    """
    function get called when user already authenticated and
     flask-jwt verified thier authorization header is correct
    :param payload: a dictionary with 'identity' key wjich is the user id
    :return: usermodel object
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
