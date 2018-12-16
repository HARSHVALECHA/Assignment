from django.contrib import admin
from .models import *
# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ('date','id','login','repos_url',)
    search_fields = ['date','id', 'login' ]


admin.site.register(github,SearchAdmin)