''' admin page python source code of product app '''
from django.contrib import admin
from .models import Product



class PorductAdmin(admin.ModelAdmin):
    ''' display name and price '''
    list_diplay = ('name', 'price',)


admin.site.register(Product, PorductAdmin)
