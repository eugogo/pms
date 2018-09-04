from  rest_framework import serializers

from uum.models import UumImg
from uum.serializer import *
from uum.serializer import role_serializer


class ImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = UumImg
        fields = '__all__'

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                obj = UumImg.objects.get(id=id)
                if obj is not None and obj.id > 0:
                    return self.update(obj, validated_data)
            else:
                raise serializers.ValidationError("no role for this pk")
        else:
            return self.create(validated_data)
