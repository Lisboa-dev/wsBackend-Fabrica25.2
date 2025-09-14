
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClusterViewSet, ClusterApi


consult=ClusterApi

router = DefaultRouter()
router.register('cluster', ClusterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Get/', consult.ClusterAPI_Consult),
  
]

