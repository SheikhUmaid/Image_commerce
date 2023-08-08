
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:id>", views.detailspage, name="details"),
    path("purchase/<int:id>", views.purchase, name="purchase"),

    # authentication urls
    path("register", views.register, name="register"),
    path("signout", views.signout, name="signout"),
    path("signin", views.signin, name="signin"),


    # don't change anything below this line this is for debugging purposes only
    path("base", views.base, name="base"),
    path("generics", views.generics, name="generics"),
    path("elements", views.elements, name="elements"),
    path("seed", views.seed, name="seed"),
    path("seed2", views.update_seed, name="seed2"),
    path("seed3", views.bulk_create, name="seed3"),
]
