from rest_framework import serializers
from mam.models import *
from mam.serializers import matgroup_task_ser, matgroup_user_ser


class Serializer(serializers.ModelSerializer):
    users = matgroup_task_ser.Serializer(many=True)
    tasks = matgroup_user_ser.Serializer(many=True)

    class Meta:
        model = MamMatgroup
        # fields = ('__all__', )
        fields = ('__all__', 'users', 'tasks')
        depth = 1

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                obj = type(self).objects.filter(id=id)
                if obj is not None and obj.id > 0:
                    return self.update(obj, validated_data)
            else:
                raise serializers.ValidationError("no task for this pk")
        else:
            return self.create(validated_data)

