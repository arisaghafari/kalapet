from django.urls import include, path, re_path
from .views import *

urlpatterns = [
    path('list/', AdvertismentList.as_view()),
    path('detail/<int:pk>/', AdvertismentDetail.as_view()),
    path('product/filter/', ProductList.as_view()),
    path('product/create/', CProductList.as_view()),
    path('vet/list/', VetList.as_view()),
    path('vet/detail/<int:pk>/', VetDetail.as_view()),
    path('me/', meAdd().as_view()),
]