from rest_framework import serializers
from core.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'full_name',
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_suspended',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
