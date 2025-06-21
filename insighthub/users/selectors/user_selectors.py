from rest_framework.exceptions import ValidationError

from insighthub.users.models import User


def get_all_users()->list[User]:
    """
    get all users from database
    :return: list of users
    """

    try:
        return User.objects.all()
    except Exception as e:
        raise ValidationError(f"can not fetch users from database : {e}")

def get_user_by_id(user_id: int)->User:
    """
    get user by id
    :param
        user_id: user id for fetch user from database
    :return:
        return user instance
    """
    try:
        return User.objects.get(id=user_id)
    except Exception as e:
        raise ValidationError(f"User by id {user_id} not found.")
