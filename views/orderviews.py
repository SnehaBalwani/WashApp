from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import LaundryShop, Garment , Contact, Orders, OrderUpdate
from math import ceil
import json
from users.forms import ProfileUpdateForm, PriceSchemeUpdateForm
from django.views.generic import ListView, CreateView


def logged_in(request):
    return render(request, 'users/laundry_home.html')


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = LaundryShop.objects.values('area', 'shop_id')
    cats = {item['area'] for item in catprods}
    for cat in cats:
        prod = LaundryShop.objects.filter(area=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}# products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4)
    return render(request, 'users/index.html', params)


def about(request):
    return render(request, 'users/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'users/contact.html')


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'users/tracker.html')


def search(request):
    return render(request, 'users/search.html')


def pricescheme(request):
    items = Garment.objects.all()
    print(items)

    return render(request, 'users/pricescheme.html', {'items': items})

class ListPriceSchemeView(ListView):
    context = Garment.objects.all()
    model = Garment
    template_name = 'users/pricescheme.html'
    context_object_name = context


class UpdatePriceSchemeView(CreateView):
    model = Garment
    form_class = PriceSchemeUpdateForm
    #template_name = 'users/update_priceschem.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'laundry_shop'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        garment = form.save()
        #login(self.request, user)
        return redirect('/update_price_scheme/')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'users/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'users/checkout.html')


#def view_profile(request):

#def price_scheme_update(request):



#@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
    else:

        form = ProfileUpdateForm(instance=request.user.profile)

    if form.is_valid():
        form.save()


    context = {'form': form}

    return render(request, 'users/update_profile.html', context)
