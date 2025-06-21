
from rest_framework.exceptions import ValidationError

from insighthub.users.interfaces.user_interface import UserInterface, UserPutInterface, UserPatchInterface
from insighthub.users.models import User


def create_user(user_interface: UserInterface)->User:
    """
    create new user
    :param
        user_interface: UserInterface object
    :return:
        created user
    """
    try:
        user  =User.objects.create(     first_name= user_interface.first_name or "",
                                        last_name= user_interface.last_name or "",
                                        username=user_interface.username,
                                        email=user_interface.email,

                                    )
        user.set_password(user_interface.password)
        user.save()
        return user
    except Exception as e:
        raise ValidationError(f"can not create new user: {e}")

def full_update_user( user_interface: UserPutInterface, user: User)->User:
    """
    user full update

    :params
        user_interface: user interface that contains new data
        user: user instance that will update

    :return:
    updated user
    """
    try:
        user.first_name = user_interface.first_name
        user.last_name = user_interface.last_name
        user.username = user_interface.username
        user.email=user_interface.email
        user.save()
        return user
    except Exception as e:
        raise ValidationError(f"can not update user {user.username}: {e}")

def partial_update_user(user_interface: UserPatchInterface, user:User)->User:
    """
    partial update user
    :params

     user_interface: An interface containing partial user update details.
     user: user instance to be updated

    :return:
       User: The updated user instance.
    """
    try:
        update_data = user_interface.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if value:
                setattr(user,field,value)
        user.save()
        return user
    except Exception as e:
        raise ValidationError(f"can not update user{user.username}: {e}")

def delete_user(user:User):
    """
        delete user
    params:
        user: user instance that will delete
    :return:
        None
    """
    try:
        user.delete()
    except Exception as e:
        raise ValidationError(f"can not delete user {user.name}: {e}")

