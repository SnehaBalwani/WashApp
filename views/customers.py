from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.shortcuts import render

from ..forms import CustomerSignUpForm
from ..models import User

def customer_login(request):
    return render(request, 'users/customer_login')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/customer_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users/customer_login')