from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='registration')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='registration_logo/', blank=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Meal(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='meal_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES = (
        (COOKING, "Cooking"),
        (READY, "Ready"),
        (ONTHEWAY, "On the way"),
        (DELIVERED, "Delivered"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, blank = True, null = True, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices = STATUS_CHOICES)
    created_at = models.DateTimeField(default = timezone.now)
    picked_at = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)

class PaytmHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_payment', on_delete=models.CASCADE)
    TXNID = models.CharField('TNX ID', max_length=70)
    BANKTXNID = models.CharField('BANK TXN ID', max_length=60, null=True, blank=True)
    ORDERID = models.CharField('ORDER ID', max_length=70)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    STATUS = models.CharField('STATUS', max_length=30)
    TXNTYPE=models.CharField('TNX TYPE', max_length=10, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=20, null=True, blank=True)
    RESPCODE = models.CharField('STATUS', max_length=20)
    RESPMSG = models.TextField('RESP MSG', max_length=600)
    BANKNAME = models.CharField('BANK NAME', max_length=600, null=True, blank=True)
    MID = models.CharField(max_length=40)
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=20, null=True, blank=True)
    REFUNDAMT = models.FloatField('RFUND AMOUNT',default=0)
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
    #CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)

    def __unicode__(self):
        return self.STATUS

