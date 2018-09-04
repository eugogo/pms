from rest_framework import serializers
from uum.models import UumPermission
from uum.serializer import role_serializer


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UumPermission
        fields = '__all__'
        # depth = 1

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "id"):
            id = validated_data.id
            if id is not None and id > 0:
                permission = UumPermission.objects.get(id=id)
                if permission is not None and permission.id > 0:
                    return self.update(permission, validated_data)
            else:
                raise serializers.ValidationError("no task for this pk")
        else:
            return self.create(validated_data)

#
# class PermissionDetailSerializer(PermissionSerializer):
#     roles = role_serializer.RoleSerializer(many=True)
#
#     class Meta:
#         model = UumPermission
#         fields = ('__all__', 'assigns', 'requirements')
#         depth = 1
