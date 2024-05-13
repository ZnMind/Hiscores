#from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlayersViewSet.as_view()),
    path("woodcutting/", views.WoodcuttingViewSet.as_view()),
]