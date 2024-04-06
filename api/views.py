from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer