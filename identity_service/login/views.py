from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users

class CreateAPI(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new loginlist."""
        serializer.save()
