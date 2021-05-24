from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your views here.

@login_required
def index(request):
    index_dict = {}

    return render(request, 'shop/index.html',context=index_dict)


@login_required
def weapons(request):
    weapons_dict = {}

    weapons = list(Product.objects.filter(category='W'))

    weapons_dict['Weapons'] = weapons

    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        req_dict = request.POST

        item_id = int(req_dict['item'])

        item_obj = Product.objects.get(id = item_id)

        order_str = str(item_id)+'  '+ str(item_obj.name)+ '  '+ user.username + '\n'
        f = open('shop/orders.txt','a')
        print(order_str)
        f.write(order_str)
        f.close()
        return redirect('/order_success')
    return render(request,'shop/weapons.html',context=weapons_dict)

@login_required
def order_success(request):
    os_dict = {}
    return render(request, 'shop/order_success.html', context=os_dict)