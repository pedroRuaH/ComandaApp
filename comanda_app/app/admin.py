from django.contrib import admin
from .models import Item, Table, Order, OrderItem, Payment, waiter, Customer
from import_export.admin import ImportExportModelAdmin

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'available', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('available',)

@admin.register(Table)
class TableAdmin(ImportExportModelAdmin):
    list_display = ('number', 'seats')
    search_fields = ('number',)

@admin.register(waiter)
class WaiterAdmin(ImportExportModelAdmin):
    list_display = ('name', 'employee_id', 'is_active', 'hired_date')
    search_fields = ('name', 'employee_id')
    list_filter = ('is_active',)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'customer', 'waiter', 'table', 'order_type', 'is_completed', 'created_at')
    list_filter = ('order_type', 'is_completed', 'created_at')
    search_fields = ('id', 'customer__name', 'waiter__name', 'table__number')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ('order', 'item', 'quantity')
    search_fields = ('order__id', 'item__name')

@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'payment_date')
    search_fields = ('order__id', 'payment_method')