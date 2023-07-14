from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # OneToOne field is meant to stop users from having the same username.
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # using pillow for showing pictures.

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):  # the whole order!
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)  # doesnt let the date stay empty
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        # کاری میکنیم که یک شماره ردیف برگردونه چون هیچکدام نمیتونه مشخصه دقیقی باشه

    @property  # to get the total sum
    def get_cart_total(self):
        cart_items = self.orderitem_set.all()
        total = sum(item.get_total for item in cart_items)
        return total

    @property  # to get the quantity of all
    def get_cart_items(self):
        cart_items = self.orderitem_set.all()
        total = sum(item.quantity for item in cart_items)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.id)


class ShippingAddress(models.Model):
    # from customer to Customer and from order to Order
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

# now to use this in db mode we use <<migrate>>
# open terminal -> py manage.py makemigrations -> if no problerm -> py manage.py migrate -> all should be ok.
# don't forget the admin file!
