from .models import Employee, Client, Product, Order
from django.contrib import admin
from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['price']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birthday']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birthday']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'employee', 'date', 'price']
    form = OrderForm


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
