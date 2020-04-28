from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import LaundryShop, Garment
from PIL import Image



from users.models import Customer, User


class PhoneNumberField(forms.Field):
    def validate_phone_number(value):
        if ((value>9999999999) and (value<=999999999)):
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )
class PinCodeField(forms.Field):

    def validate_pin_code(value):
        if ((value>999999) and (value<=99999)):
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )

# class AreaField(forms.Field):
#     AREA_CHOICES = ['matunga', 'vadala', 'sion', 'dadar', 'bandra']
#     def validate(self,value):
#         if(value not in AREA_CHOICES )
#


class CustomerSignUpForm(UserCreationForm):

    AREA_CHOICES = ['matunga', 'vadala', 'sion', 'dadar', 'bandra']
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=500)
    pin_code = forms.CharField(max_length=20)
    area = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        self.cleaned_data.get('email')
        self.cleaned_data.get('first_name')
        self.cleaned_data.get('last_name')
        self.cleaned_data.get('phone_number')
        self.cleaned_data.get('address')
        self.cleaned_data.get('pin_code')
        self.cleaned_data.get('area')

        return user


class LaundryShopSignUpForm(UserCreationForm):
    email = forms.EmailField()
    shop_name = forms.CharField(max_length=30)
    owner_name = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=500)
    pin_code = forms.CharField(max_length=20)
    area = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'shop_name', 'owner_name', 'phone_number', 'address', 'pin_code', 'area', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_laundry_shop = True
        user.save()

        laundry_shop = LaundryShop.objects.create(user=user)
        self.cleaned_data.get('email')
        self.cleaned_data.get('shop_name')
        self.cleaned_data.get('owner_name')
        self.cleaned_data.get('phone_number')
        self.cleaned_data.get('address')
        self.cleaned_data.get('pin_code')
        self.cleaned_data.get('area')

        return user



class ProfileUpdateForm(forms.ModelForm):
    # shirt_price = forms.IntegerField()
    # pant_price = forms.IntegerField()
    # top_price = forms.IntegerField()
    # jeans_price = forms.IntegerField()
    # def save_img(self):
    #     super.save()
    #     img = Image.open(self.image.path)
    #     if img.height >300 or img.width>300 :
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


    class Meta:
        model = LaundryShop
        fields = ['image']


class PriceSchemeUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()

    class Meta:
        model = Garment
        fields = ['name', 'price']


