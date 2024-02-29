from django.contrib import admin
from django.urls import path, include
from rest.views import RegularUserListCreate
from rest.views import ShopListCreate
from rest.views import ShopListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('registration/', include('registration.urls', namespace='registration')), 
    path('login/', include('login.urls', namespace='login')),
    path('api/users/', RegularUserListCreate.as_view()),
    path('api/shops/', ShopListCreate.as_view()),
    path('allGames/', ShopListAPIView.as_view()),
]