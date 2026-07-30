from rest_framework.pagination import PageNumberPagination

class DevicePagination(PageNumberPagination):

    page_size = 5