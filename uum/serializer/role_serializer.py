from rest_framework import serializers
from uum.models import UumRole
from uum.serializer import user_serializer, permission_serializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UumRole
        fields = '__all__'
        # depth = 1

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                role = UumRole.objects.get(id=id)
                if role is not None and role.id > 0:
                    return self.update(role, validated_data)
            else:
                raise serializers.ValidationError("no task for this pk")
        else:
            return self.create(validated_data)


class RoleDetailSerializer(RoleSerializer):
    # users = user_serializer.UserSerializer(many=True)
    permissions = permission_serializer.PermissionSerializer(many=True)

    class Meta:
        model = UumRole
        # fields = '__all__'
        fields = ('__all__', 'users', 'permissions')
        depth = 1
