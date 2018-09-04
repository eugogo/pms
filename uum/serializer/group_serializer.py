from rest_framework import serializers
from uum.models import UumGroup
from uum.serializer import user_serializer


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UumGroup
        fields = ('__all__')

    def create_or_update(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                obj = UumGroup.objects.get(id=id)
                if obj is not None and obj.id > 0:
                    return self.update(obj, validated_data)
            else:
                raise serializers.ValidationError("no role for this pk")
        else:
            return self.create(validated_data)


class GroupDetailSerializer(GroupSerializer):
    # users = user_serializer.UserSerializer(many=True)

    class Meta:
        model = UumGroup
        fields = ('__all__', 'groups', 'roles')
        # fields = ('task_id', 'task_code', 'task_name', 'assigns', 'requirements')
        depth = 1
