from rest_framework import serializers
from tco_app.models import SystemTable, ModelTable

class ModelNameSerializer(serializers.ModelSerializer):
    system_name = serializers.RelatedField(source='SystemTable', read_only=True)

    class Meta:
        model = ModelTable
        fields = ('system_name')
