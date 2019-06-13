from django.urls import include, path
from .views import *

urlpatterns = [
    path('list', AdvertismentList.as_view()),
    path('detail/<int:pk>/', AdvertismentDetail.as_view()),
]