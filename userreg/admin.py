from django.contrib import admin
from .models import register_model, address
# Register your models here.


admin.site.register(register_model)

admin.site.register(address)