from django.db import models
from django.contrib.auth.models import User



class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    info = models.TextField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name + "-" + self.food.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    delivery_address = models.TextField(max_length=255)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer_info = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_date = models.DateField(blank=True)
    product = models.ManyToManyField(Menu)
    PAYMENT_METHOD_CHOICES = (
        ('CH', 'Cash'),
        ('CD', 'Card')
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )
    ORDER_STATUS_CHOICES = (
        ('CF', 'Confirmed'),
        ('R', 'Ready'),
        ('S', 'Send'),
        ('D', 'Delivered'),
        ('R', 'Returned'),
        ('C', 'Cancelled')
    )
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.customer_info.name.username + "-" + str(self.id)