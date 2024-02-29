from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import RegularUserSerializer, ShopSerializer
from .pagination import CustomPagination
from registration.models import Regular_User
from main.models import Shop

class RegularUserListCreate(generics.ListCreateAPIView):
    """
    API view to list and create regular users.

    Inherits from: rest_framework.generics.ListCreateAPIView

    Methods:
    - GET: Retrieve a list of regular users.
    - POST: Create a new regular user.
    - PUT: Update an existing regular user.
    - DELETE: Delete an existing regular user.
    """

    queryset = Regular_User.objects.all()
    serializer_class = RegularUserSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a list of regular users.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new regular user.
        """
        self.create(request, *args, **kwargs)
        instance = Regular_User.objects.latest('id')
        serializer = self.get_serializer(instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update an existing regular user.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete an existing regular user.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

class ShopListCreate(generics.ListCreateAPIView):
    """
    API view to list and create shops.

    Inherits from: rest_framework.generics.ListCreateAPIView

    Methods:
    - GET: Retrieve a list of shops.
    - POST: Create a new shop.
    """

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a list of shops.
        """
        queryset = self.filter_queryset(self.get_queryset())[:20]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ShopListAPIView(ListAPIView):
    """
    API view to list shops with pagination.

    Inherits from: rest_framework.generics.ListAPIView

    Methods:
    - GET: Retrieve a paginated list of shops.
    """

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a paginated list of shops.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)