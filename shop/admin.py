from django.contrib import admin

# Register your models here.
from .models import product,Contact,Checkout

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Checkout)