
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status

from insighthub.api.mixins import ApiAuthAdmin
from insighthub.api.pagination import get_paginated_response_context
from insighthub.api.serializer import PaginationFilterSerializer
from insighthub.users.apis.users.serializers.serializers import UserListCreateSerializer, UserOutputSerializer
from insighthub.users.apis.users.serializers.swagger_serializers import UserListSwaggerSerializer, \
    UserSwaggerOutPutSerializer
from insighthub.users.constants import USER_TAGS
from insighthub.users.interfaces.user_interface import UserInterface
from insighthub.users.models import User
from insighthub.users.selectors.user_selectors import get_all_users
from insighthub.users.services.user_services import create_user
from insighthub.utils.pagination import CustomPaginationPagination


class UserListCreateApi(ApiAuthAdmin, APIView):

    queryset = User.objects.all()

    @extend_schema(tags=USER_TAGS, responses=UserListSwaggerSerializer, parameters=[PaginationFilterSerializer])
    def get(self, request):
        users = get_all_users()

        return get_paginated_response_context(
            pagination_class=CustomPaginationPagination,
            serializer_class= UserListCreateSerializer,
            queryset=users,
            request= request,
            view=self
        )

    @extend_schema(tags=USER_TAGS, request=UserListCreateSerializer, responses=UserSwaggerOutPutSerializer)
    def post(self, request):
        serializer = UserListCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_interfaced = UserInterface(
            first_name= serializer.validated_data.get("first_name",None),
            last_name= serializer.validated_data.get("last_name",None),
            username= serializer.validated_data.get("username"),
            email= serializer.validated_data.get("email"),
            password= serializer.validated_data.get("password"),
        )

        user = create_user(user_interfaced)
        return Response(UserOutputSerializer(instance=user).data, status=status.HTTP_201_CREATED)

