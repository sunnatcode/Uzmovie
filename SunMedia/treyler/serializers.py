from rest_framework.serializers import ModelSerializer
from .models import Treyler

class TreylerSerializers(ModelSerializer):
    class Meta:
        model = Treyler
        fields = ['title', 'description', 'startYear', 'endYear']