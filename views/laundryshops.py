from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.shortcuts import render
from ..models import LaundryShop
from ..forms import LaundryShopSignUpForm
from ..models import User


def laundry_login(request):
    return render(request, 'users/laundry_login')


class LaundryShopSignUpView(CreateView):
    model = LaundryShop
    form_class = LaundryShopSignUpForm
    template_name = 'users/laundry_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'laundry_shop'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users/laundry_home')