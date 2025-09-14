from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializer import  UserCreateSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserCreateSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
