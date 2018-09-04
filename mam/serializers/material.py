from rest_framework import serializers
from mam.models import MamMaterial, MamCata, MamCataExt
from task.serializer import task_assign_serializer, task_requirement_serializer




class CataExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamCataExt
        fields = ('__all__',)
        # depth = 1


class CheckSerializer(serializers.ModelSerializer):
    # cataExt = task_requirement_serializer.TaskRequirementSerializer(many=True)
    class Meta:
        model = MamCata
        fields = ('__all__',)
        # depth = 1

class MaterialSerializer(serializers.ModelSerializer):
    cata_ser = CataSerializer()
    # requirements = task_requirement_serializer.TaskRequirementSerializer(many=True)

    class Meta:
        model = MamMaterial
        fields = ('__all__', 'assigns', 'requirements')
        depth = 1

    def create_or_updata(self, validated_data):
        if hasattr(validated_data, "task_id"):
            task_id = validated_data.task_id
            if task_id is not None and task_id > 0:
                task = Task.objects.get(task_id=task_id)
                if task is not None and task.task_id > 0:
                    return self.update(task, validated_data)
            else:
                raise serializers.ValidationError("no task for this pk")
        else:
            return self.create(validated_data)

