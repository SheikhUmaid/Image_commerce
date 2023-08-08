from django.shortcuts import render, redirect
from .models import Product
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout, get_user_model
import razorpay
from django.conf import settings
from django.db.models import Q

User = get_user_model()


def index(request):
    search_query = request.GET.get("search", "")

    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = range(1,paginator.num_pages+1)
    latest_product = Product.objects.first()
    context = {"products": page_obj, "total_pages": total_pages, "latest_product": latest_product, "index_activity": "active"}
    if search_query:
        products = Product.objects.filter(Q(product_name__icontains=search_query) | Q(product_desc__icontains=search_query))
        context["products"] = products
        context["search_query"] = search_query
        return render(request, "index.html",  context)
    return render(request, "index.html",  context)


def detailspage(request, id):
    product = Product.objects.get(id=id)
    user = request.user
    context = {"product": product}
    if request.user.is_authenticated:
        if user.products_purchased.filter(id=id).exists():
            context["purchased"] = True

    if request.method == "POST":
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': product.product_price, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        product.product_payment_id = payment["id"]
        product.save()
        context = {"product": product, "payment": payment}
        return render(request, "detailpage.html", context)
    return render(request, "detailpage.html", context)


def purchase(request, id):
    product = Product.objects.get(id=id)
    user = request.user
    dir(user)
    user.products_purchased.add(product)
    print(user.products_purchased.all())
    # return HttpResponse("Purchased")
    return redirect("details", id=id)






# authentication views
def register(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        else:
            user = User.objects.create_user(name=name, email=email, password=password1)
            user.save()
            return redirect("signin")


    context = {"register_activity": "active"}
    return render(request, "register.html", context)

def signin(request):
    context = {"signin_activity": "active"}
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, "signin.html", context)



def signout(request):
    logout(request)
    return redirect("index")









# Don't change anything below this line this is for debugging purposes only

def base(request):
    return render(request, "base.html")


def seed(request):

    image = "images/seedimage.jpeg"

    
    description = "This is a seed image for the product description."


    # make some products some realist names and descriptions
    
    for i in range(61, 121):
        Product.objects.create(product_name="Product " + str(i), product_desc=f"Product {i} description, {description}", product_price=i * 10, product_image=image)
    return HttpResponse("Seeded")


def update_seed(request):
    products = Product.objects.all()
    image = "images/seedimage.jpeg"
    for product in products:
        product.product_file = 'files/db.sqlite3'
        product.product_image = image
        product.save()
    return HttpResponse("Updated")


def elements(request):

    return render(request, "elements.html")

def generics(request):
    return render(request, "generic.html")

def bulk_create(request):
    product1 = Product.objects.create(
    product_name="Smartphone X",
    product_desc="A high-performance smartphone with advanced features.",
    product_price=799,
    product_image="smartphone_x.jpg",
    # product_date="2023-08-07 10:00:00",
    ).save()

    product2 = Product.objects.create(
        product_name="Laptop Pro",
        product_desc="Powerful laptop for professionals, ideal for multitasking and creative work.",
        product_price=1499,
        product_image="laptop_pro.jpg",
        product_file="laptop_pro_spec.pdf",
        # product_date="2023-08-06 15:30:00",
    ).save()

    product3 = Product.objects.create(
        product_name="Wireless Earbuds",
        product_desc="Enjoy crystal-clear sound with these wireless earbuds. Perfect for music lovers.",
        product_price=99,
        product_image="wireless_earbuds.jpg",
        # product_date="2023-08-05 09:45:00",
        product_payment_id="PAY123456",
    ).save()

    product4 = Product.objects.create(
        product_name="Fitness Tracker",
        product_desc="Track your health and fitness goals with this smart fitness tracker.",
        product_price=49,
        product_image="fitness_tracker.jpg",
        # product_date="2023-08-04 18:20:00",
        product_payment_id="PAY789012",
    ).save()
    return HttpResponse("Bulk Created")