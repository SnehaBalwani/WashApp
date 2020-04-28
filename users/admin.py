from django.contrib import admin
from.models import  Customer, LaundryShop

from .models import Contact, Orders, OrderUpdate,Garment

admin.site.register(Contact)
admin.site.register(Garment)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

admin.site.register(Customer)
admin.site.register(LaundryShop)
# Register your models here.
