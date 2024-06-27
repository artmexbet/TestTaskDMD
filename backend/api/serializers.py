from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'performers', 'registration_date', 'status', 'planned_effort',
                  'actual_effort', 'completion_date', 'parent_task']
