from django.contrib import admin
from .models import Mouse, Feeding

# Register your models here.
admin.site.register(Mouse)
# register the new Feeding Model 
admin.site.register(Feeding)
