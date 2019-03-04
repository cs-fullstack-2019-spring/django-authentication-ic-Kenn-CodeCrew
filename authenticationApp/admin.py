from django.contrib import admin
from .models import DMVModel, BankAccountModel

# Register your models here.
admin.site.register(DMVModel)
admin.site.register(BankAccountModel)