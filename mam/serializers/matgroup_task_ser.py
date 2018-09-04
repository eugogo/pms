from  rest_framework import serializers
from mam.models import *



class Serializer(serializers.ModelSerializer):
    # users = task_assign_serializer.TaskAssignSerializer(many=True)
    # tasks = task_requirement_serializer.TaskRequirementSerializer(many=True)

    class Meta:
        model = MamMatgroupTask
        fields = ('__all__', )
        # fields = ('__all__', 'assigns', 'requirements')
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


