
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from insighthub.api.mixins import ApiAuthAdmin
from insighthub.api.pagination import get_paginated_response_context, LimitOffsetPagination
from insighthub.users.apis.users.serializers.serializers import UserListCreateSerializer
from insighthub.users.apis.users.serializers.swagger_serializers import UserListSwaggerSerializer
from insighthub.users.constants import USER_TAGS
from insighthub.users.models import User
# from insighthub.users.interfaces.user_interface import UserInterface
from insighthub.users.selectors.user_selectors import get_all_users


class UserListCreateApi(ApiAuthAdmin, APIView):

    queryset = User.objects.all()

    @extend_schema(tags=USER_TAGS, responses=UserListSwaggerSerializer)
    def get(self, request):
        users = get_all_users()

        return get_paginated_response_context(
            pagination_class=LimitOffsetPagination,
            serializer_class= UserListCreateSerializer,
            queryset=users,
            request= request,
            view=self
        )

