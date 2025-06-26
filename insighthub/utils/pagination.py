from rest_framework.pagination import PageNumberPagination

class CustomPaginationPagination(PageNumberPagination):
    def get_page_size(self, request):
        """
        set page size

        """
        if request.query_params.get('page_size'):
            return request.query_params.get('page_size')
        elif  request.user.is_superuser:
            return 100 # For admin users
        return 10  # For regular users

    def get_page_number(self, request, paginator):
        """
        set page number

        """
        if request.query_params.get('page'):
            return request.query_params.get('page')
        return 1