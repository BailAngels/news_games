from django.urls import path

from apps.publishers.views import  (
    list_publishers,
    detail_publisher

)

urlpatterns = [
    path('publisher/', list_publishers, name='list_publishers'),
    path('publisher/<int:pk>', detail_publisher, name='detail_publisher'),
]