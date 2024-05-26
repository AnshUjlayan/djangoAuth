from django.urls import path
from auth.views import MyTokenObtainPairView, hello, please
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("please/", please, name="please"),
    path("hello/", hello, name="hello"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
