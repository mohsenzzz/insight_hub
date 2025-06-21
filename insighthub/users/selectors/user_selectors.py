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