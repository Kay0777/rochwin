from rest_framework import serializers
from .models import Employee, Client, Product, Order


class ResponseDataToRepresentation(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            'total_clients': instance.total_clients,
            'total_items_sold': instance.total_items_sold,
            'total_sales': instance.total_sales
        })
        return data


class EmployeeSerializer(ResponseDataToRepresentation):
    class Meta:
        model = Employee
        fields = ['full_name']


class AllEmployeesSerializer(ResponseDataToRepresentation):
    class Meta:
        model = Employee
        fields = ['id', 'full_name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            'total_purchased_items': instance.total_purchased_items,
            'total_sales': instance.total_sales
        })
        return data
