from django.urls import path
from . import views
from rest.views import RegularUserListCreate
from rest.views import ShopListCreate, TopListCreate
from .views import ShopListAPIView

app_name = 'rest'

urlpatterns = [
    path('', views.RegularUserListCreate.as_view(), name='regular_user-list-create'),
    path('', views.ShopListCreate.as_view(), name='regular_user-list-create'),
    path('', views.TopListCreate.as_view(), name='regular_game-list-create'),
    path('', ShopListAPIView.as_view(), name='shop-list'),
]