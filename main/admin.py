from django.contrib import admin

# Register your models here.
from main.models import *


class modelStreet(admin.ModelAdmin):
    pass


admin.site.register(Street, modelStreet)
