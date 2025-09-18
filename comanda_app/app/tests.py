from django.test import TestCase
from .models import Item, waiter, Table, Customer, Order, OrderItem, Payment

class RestaurantModelsTest(TestCase):
    def setUp(self):
        self.item1 = Item.objects.create(name="Pizza", price=10.00)
        self.item2 = Item.objects.create(name="Pasta", price=8.50)
        self.waiter = waiter.objects.create(name="Alice", employee_id="W001")
        self.table = Table.objects.create(number=1, seats=4)
        self.customer = Customer.objects.create(name="Bob")
        self.order = Order.objects.create(
            customer=self.customer,
            waiter=self.waiter,
            table=self.table,
            order_type='dine_in'
        )
        self.order_item1 = OrderItem.objects.create(order=self.order, item=self.item1, quantity=2)
        self.order_item2 = OrderItem.objects.create(order=self.order, item=self.item2, quantity=1)

    def test_order_total_amount(self):
        total = self.order.get_total_amount()
        expected = (self.item1.price * 2) + (self.item2.price * 1)
        self.assertEqual(total, expected)

    def test_payment_amount_auto_set(self):
        payment = Payment(order=self.order, payment_method="cash")
        payment.save()
        self.assertEqual(payment.amount, self.order.get_total_amount())

    def test_order_str(self):
        self.assertIn("Order #", str(self.order))
        self.assertIn(self.table.__str__(), str(self.order))

    def test_orderitem_str(self):
        self.assertEqual(
            str(self.order_item1),
            f"2 x {self.item1.name} (Order #{self.order.id})"
        )

    def test_payment_str(self):
        payment = Payment(order=self.order, payment_method="card")
        payment.save()
        self.assertIn(f"Payment for Order #{self.order.id}", str(payment))
