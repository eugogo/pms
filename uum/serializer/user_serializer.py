from rest_framework import serializers
from uum.models import UumUser
from uum.serializer import role_serializer, group_serializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UumUser
        fields = ('__all__')

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                role = UumUser.objects.get(id=id)
                if role is not None and role.id > 0:
                    return self.update(role, validated_data)
            else:
                raise serializers.ValidationError("no role for this pk")
        else:
            return self.create(validated_data)


class UserDetailSerializer(UserSerializer):
    groups = group_serializer.GroupSerializer(many=True)
    roles = role_serializer.RoleSerializer(many=True)
    # img = img_serializer.imgSerializer()

    class Meta:
        model = UumUser
        fields = ('__all__', 'groups', 'roles')
        # fields = ('task_id', 'task_code', 'task_name', 'assigns', 'requirements')
        depth = 1
