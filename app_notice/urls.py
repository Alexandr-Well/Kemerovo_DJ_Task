
from django.urls import path


from .views import MainPage, NoticeDetail, UserNotice

urlpatterns = [
    path('main/', MainPage.as_view(), name="main"),
    path('main/<int:pk>', NoticeDetail.as_view(), name="notice_detail"),
    path('user_notice/', UserNotice.as_view(), name="users_notice"),

]