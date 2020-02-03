''' admin source code of order app '''
from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    ''' display user and product list '''
    list_display = ('user', 'product')


admin.site.register(Order, OrderAdmin)
