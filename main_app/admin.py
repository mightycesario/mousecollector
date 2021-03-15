from django.contrib import admin
from .models import Mouse, Feeding, Toy

# Register your models here.
admin.site.register(Mouse)
admin.site.register(Feeding)
admin.site.register(Toy)