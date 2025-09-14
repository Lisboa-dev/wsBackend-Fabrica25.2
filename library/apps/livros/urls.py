

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  BookApi


consult=BookApi

urlpatterns = [
    path('Get/', consult.BookAPI_Consult),
    path('Post/', consult.BookAPI_Save),
    path('Delete/<int:id>/', consult.BookAPI_Delete),
]

