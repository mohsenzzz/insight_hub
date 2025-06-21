
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import status

from insighthub.api.mixins import ApiAuthMixin
from insighthub.users.apis.users.serializers.serializers import UserOutputSerializer, UserPutSerializer, \
    UserPatchSerializer
from insighthub.users.apis.users.serializers.swagger_serializers import UserSwaggerOutPutSerializer
from insighthub.users.constants import USER_TAGS
from insighthub.users.interfaces.user_interface import UserInterface, UserPutInterface, UserPatchInterface
from insighthub.users.selectors.user_selectors import get_user_by_id
from insighthub.users.services.user_services import full_update_user, partial_update_user, delete_user


class UserRetrieveUpdateDeleteApi(ApiAuthMixin, APIView):

    @extend_schema(tags=USER_TAGS, responses=UserSwaggerOutPutSerializer)
    def get(self, request, user_id):
        user = get_user_by_id(user_id)

        return Response(UserOutputSerializer(instance=user).data, status=status.HTTP_200_OK)

    @extend_schema(tags=USER_TAGS, request=UserPutSerializer, responses=UserSwaggerOutPutSerializer)
    def put(self, request, user_id):
        user = get_user_by_id(user_id)
        serializer = UserPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_interface = UserPutInterface(
                                        first_name= serializer.validated_data.get("first_name", None),
                                        last_name= serializer.validated_data.get("last_name", None),
                                        username= serializer.validated_data.get("username"),
                                        email= serializer.validated_data.get("email"),
        )

        user = full_update_user(user_interface=user_interface, user= user)

        return Response(UserOutputSerializer(instance=user).data, status= status.HTTP_200_OK)

    @extend_schema(tags=USER_TAGS, request=UserPatchSerializer, responses=UserSwaggerOutPutSerializer)
    def patch(self, request, user_id):
        user = get_user_by_id(user_id)
        serializer = UserPatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_interfaced = UserPatchInterface(
            first_name=serializer.validated_data.get("first_name", None),
            last_name=serializer.validated_data.get("last_name", None),
            username=serializer.validated_data.get("username", None),
            email=serializer.validated_data.get("email", None),
        )
        user= partial_update_user(user_interface=user_interfaced, user=user)
        return Response(UserOutputSerializer(instance=user).data, status= status.HTTP_200_OK)

    @extend_schema(tags=USER_TAGS, responses={204: "accepted"})
    def delete(self, request, user_id):
        user = get_user_by_id(user_id=user_id)
        delete_user(user=user)
        return Response(status=status.HTTP_204_NO_CONTENT)
