# -*- coding:utf-8 -*-

from rest_framework.pagination import PageNumberPagination


class AssetsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100