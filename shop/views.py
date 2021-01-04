# Importing necessary module

from django.shortcuts import render  # already present at django views.py
from django.http import HttpResponse  # already present at django views.py
# Importing the table from database in models
from shop.models import Product, Contact, Order, OrderUpdate
# importing ceil fuction which help in returning x the smallest integer not less than x.
from math import ceil
import json  # used for json operation
# a decorators used to make a function free from csrf security.
from django.views.decorators.csrf import csrf_exempt
import requests  # kind of module to send http response
from django.http import JsonResponse  # Type of response in django
from decouple import config

# Create your views here.


def index(request):

    # listing the product category wise
    allprods = []
    product = Product.objects.all()  # used to get all the record in table
    # taking the category and product id of record in tale
    CategoriesProduct = Product.objects.values('category', 'Product_id')
    categories = {item['category']
                  for item in CategoriesProduct}  # listing out all categories

    # cateory wise making list of list of item in same category
    for category in categories:
        prods = Product.objects.filter(category=category)
        n = len(prods)
        nslide = n//4 + ceil((n/4)-(n//4))
        allprods.append([prods, range(1, nslide), nslide])
    params = {
        'allProds': allprods
    }
    # returning the template and params which is ccategory wise product
    return render(request, "shop/index.html", params)


def search(request):
    query = request.GET.get('search')
    allprods = []
    product = Product.objects.all()

    if query:
        for item in product:
            if query.lower() in item.Product_descr.lower() or query.lower() in item.Product_name.lower() or query.lower() in item.category.lower():
                allprods.append(item)

    else:
        return render(request, "shop/search.html", {'not': True})
    return render(request, "shop/search.html", {'allprods': allprods})


def about(request):
    # returning the about us template
    return render(request, "shop/about.html")


def contact(request):
    """ sending the data given by user to contact us table"""

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        Phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # passing the value to contact class
        contact = Contact(name=name, email=email, phone=Phone, desc=desc)
        contact.save()  # saving the contact info to contact table
    return render(request, "shop/contact.html")


def ProductView(request, myid):
    # fetching product using id
    product = Product.objects.filter(Product_id=myid)
    return render(request, "shop/ProductView.html", {'product': product[0]})


def tracker(request):
    # Fetching out all the update of order from the order update table
    responses = ""
    if request.method == 'POST':
        orderId = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            # filtering the order by order id and email
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                # fetching the order update of given order id
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []  # initializing the updates list
                for item in update:
                    # listing out the order update
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    # converting the json object to text  by using dumps() function for giving as response
                    responses = json.dumps(
                        {'status': 'success', 'updates': updates, 'itemJSon': order[0].itemJSon}, default=str)
                return HttpResponse(responses)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, "shop/tracker.html")


def checkout(request):
    if request.method == 'POST':
        # listing out the data given by user to place order .
        itemsJSon = request.POST.get('itemsJson', '')
        # listing out the data given by user to place order .
        name = request.POST.get('name', '')
        # listing out the data given by user to place order .
        amount = request.POST.get('amount', '')
        # listing out the data given by user to place order .
        email = request.POST.get('email', '')
        # listing out the data given by user to place order .
        phone = request.POST.get('phone', '')
        # listing out the data given by user to place order .
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        # listing out the data given by user to place order .
        state = request.POST.get('state', '')
        # listing out the data given by user to place order .
        city = request.POST.get('city', '')
        # listing out the data given by user to place order .
        zip_code = request.POST.get('zip_code', '')
        order = Order(itemJSon=itemsJSon, amount=amount, name=name, email=email, phone=phone,
                      address=address, state=state, city=city, zip_code=zip_code)  # passig value at order class
        order.save()  # saving the data in table
        global id_order
        id_order = order.order_id
        thanks = True

        return render(request, "shop/payment.html", {'thanks': thanks, 'id': id_order, })

    return render(request, "shop/checkout.html")


@csrf_exempt
def verifyPayment(request):
    data = request.POST  # getting the data send by the ajax to verify
    token = data['token']  # getting the token from the data send from page
    amount = data['amount']  # getting the amount from the data send from page
    """ sending the data to khalti for verification """
    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
        "token": token,
        "amount": amount
    }
    headers = {
        "Authorization": config("TEST_SECRET_KEY")
    }
    response = requests.post(url, payload, headers=headers)
    """ recieving the data from khalti """
    response_data = json.loads(
        response.text)  # data given by khalt and converting to json format
    # fetching the status code of payment
    status_code = str(response.status_code)

    if status_code == 400:
        response = JsonResponse(
            {'status': 'false', 'message': response_data['detail']}, status=500)
        return response
    """
    import pprint # alibrary use to print the json easily
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)
    """
    updates = OrderUpdate(
        order_id=id_order, update_desc='Your order has been placed')  # order update  initializing during checkout
    updates.save()
    return JsonResponse(response_data['user']['idx'], safe=False)
