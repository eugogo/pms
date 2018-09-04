from rest_framework import serializers
from mam.models import MamMaterial


class MamSerializer(serializers.ModelSerializer):
    # assigns = task_assign_serializer.TaskAssignSerializer(many=True)
    # requirements = task_requirement_serializer.TaskRequirementSerializer(many=True)

    class Meta:
        model = MamMaterial
        fields = ('__all__', 'assigns', 'requirements')
        depth = 1



