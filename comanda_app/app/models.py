from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"Table {self.number}"

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} - Table {self.table.number if self.table else 'N/A'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (Order #{self.order.id})"