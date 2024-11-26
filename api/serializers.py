from rest_framework import serializers
from core.models import Account, Task
import pytz
from django.utils.timezone import make_aware

def get_correct_time(obj):
    karachi_tz = pytz.timezone('Asia/Karachi')
    if obj.created_at.tzinfo is None:
        obj.created_at = make_aware(obj.created_at)
    created_at_karachi = obj.created_at.astimezone(karachi_tz)
    return created_at_karachi.strftime('%d/%m/%Y %I:%M %p')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']

    def get_created_at(self, obj):
        return get_correct_time(obj)

    def get_updated_at(self, obj):
        return get_correct_time(obj)
