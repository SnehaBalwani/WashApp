"""washapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import customers, laundryshops
from django.contrib.auth import views as auth_views
from users.views import orderviews as views
from users.views.orderviews import UpdatePriceSchemeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('customer_register/', customers.CustomerSignUpView.as_view(),name='customer_register'),
    path('customer_login/', auth_views.LoginView.as_view(template_name='users/customer_login.html'),
         name='customer_login'),
    path('customer_register/users/customer_login',auth_views.LoginView.as_view(template_name='users/customer_login.html'), name='customer_register_redirected_login'),

    path('laundry_register/', laundryshops.LaundryShopSignUpView.as_view(), name='laundry_register'),
    path('laundry_login/', auth_views.LoginView.as_view(template_name='users/laundry_login.html'), name='laundry_login'),
    path('laundry_register/users/laundry_login/',auth_views.LoginView.as_view(template_name='users/laundry_login'), name='laundry_register_redirected_login'),
    path('shop/', views.index, name='shop'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='contact'),
    path('shop/tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('pricescheme/', views.pricescheme, name='price_scheme'),
    path('shop/pricescheme/', views.pricescheme, name='add_to_cart_price_scheme'),
    path('shop/checkout/', views.checkout, name="Checkout"),
    path('profile_update',views.profile_update, name='profile_update'),
    path('laundry_home/', views.logged_in, name='laundry_home'),
    path('laundry_register/users/laundry_home/', views.logged_in, name='laundry_register_redirected_home'),
    path('update_price_scheme/', views.UpdatePriceSchemeView.as_view(), name='garment_create'),
   # path('update_price_scheme/users/laundry_home/',views.logged_in, name='update_price_scheme_redirected_home'),
    path('laundry_register/users/laundry_message/', views.laundry_message, name='laundry_message'),
    path('services/', views.services, name='services'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
