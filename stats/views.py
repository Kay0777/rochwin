from rest_framework.response import Response
from rest_framework import generics
from .models import Employee, Client, Order
from .serializers import EmployeeSerializer, AllEmployeesSerializer, ClientSerializer
from django.db.models import Count, Sum


class EmployeeStatisticsMixin:
    def get_queryset(self):
        queryset = Employee.objects.annotate(
            total_clients=Count('orders__client', distinct=True),
            total_items_sold=Count('orders__products', distinct=True),
            total_sales=Sum('orders__price')
        )

        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        if month and year:
            queryset = queryset.filter(
                orders__date__month=month, orders__date__year=year)

        return queryset


class EmployeeStatisticsView(EmployeeStatisticsMixin, generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer


class AllEmployeesStatisticsView(EmployeeStatisticsMixin, generics.ListAPIView):
    serializer_class = AllEmployeesSerializer


class ClientStatisticsView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    # возвращает – ФИО, количество клиентов, количество товаров, сумму продаж

    def get_queryset(self):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        queryset = Client.objects.annotate(
            total_purchased_items=Count('orders__products', distinct=True),
            total_sales=Sum('orders__price')
        )

        if month and year:
            queryset = queryset.filter(
                orders__date__month=month, orders__date__year=year)

        return queryset
