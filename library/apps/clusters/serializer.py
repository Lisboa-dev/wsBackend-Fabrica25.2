from .models import Clusters
from rest_framework import serializers




class serializerCluster(serializers.ModelSerializer):
    class Meta:
        model = Clusters
        fields = ["id", "name", "genres", "description", "user"]
        read_only_fields = ["user"]

