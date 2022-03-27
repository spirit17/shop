
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shop here"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TreckingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productview, name="ProductView"),
    path("productpre/", views.productpre, name="Productpre"),
    path("checkout/", views.checkout, name="Cheackout"),
]