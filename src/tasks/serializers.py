from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()

    def to_representation(self, instance):
        fields = super().to_representation(instance)
        fields["user"] = instance.user.id

        return fields

    class Meta:
        model = Task
        fields = "__all__"

class TaskUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=["pending", "in_progress", "complete"])

    def save(self, **kwargs):
        self.instance.status = self.validated_data.get("status")
        self.instance.save()
