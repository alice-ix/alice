''' admin for user '''
from django.contrib import admin
from .models import AliceUser



class AliceUserAdmin(admin.ModelAdmin):
    ''' this is admin python codee for user app '''
    list_display = ('email', )


admin.site.register(AliceUser, AliceUserAdmin)
