from django.urls import path
from .views import RegisterUser, LoginUser, logout_user, EditUserInfo, ViewUserInfo

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path("edit_user/<int:pk>", EditUserInfo.as_view(), name="cng_user_info"),
    path("user_info/", ViewUserInfo.as_view(), name="user_info"),
]