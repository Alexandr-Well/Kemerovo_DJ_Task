from django.urls import path
from .views import MainPage, NoticeDetail

urlpatterns = [
    path('main/', MainPage.as_view(), name="main"),
    path('main/<int:pk>', NoticeDetail.as_view(), name="notice_detail"),

]