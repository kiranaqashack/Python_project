from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # Name of the model is specified here
        model = Users
        # The following fields are created in the 'postgres' DB with the name 'Users'
        fields = ('id', 'name', 'password')
        # fields = ('id', 'name', 'password', 'date_created', 'date_modified')
        # read_only_fields = ('date_created', 'date_modified')