from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_laundry_shop = models.BooleanField(default=False)



class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30, default='null')
    last_name = models.CharField(max_length=30, default='null')
    phone_number = models.CharField(max_length=10, default='null')
    address = models.CharField(max_length=500, default='null')
    pin_code = models.CharField(max_length=6, default='null')
    area = models.CharField(max_length=20, default='null')

    def __str__(self):
        return f'{self.user.username} Customer'

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super.save()
    #

class LaundryShop(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shop_id = models.IntegerField(serialize=True,default=user.primary_key)
    email = models.EmailField()
    shop_name = models.CharField(max_length=30, default='null')
    owner_name = models.CharField(max_length=30, default='null')
    phone_number = models.CharField(max_length=10, default='null')
    address = models.CharField(max_length=500, default='null')
    pin_code = models.CharField(max_length=6, default='null')
    area = models.CharField(max_length=20, default='null')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)

    def save_img(self):
        super.save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width>300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return f'{self.user.username} Shop'

class Garment(models.Model):
    #garment_id = models.AutoField
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
       return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] + "..."

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # shirt_price = models.SmallIntegerField()
    # pant_price = models.SmallIntegerField()
    # top_price = models.SmallIntegerField()
    # jeans_price = models.SmallIntegerField()




