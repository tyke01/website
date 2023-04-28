from django.contrib import admin
from .models import Position, Sales, CSV


# Register your models here.
admin.site.register(Position)
admin.site.register(Sales)
admin.site.register(CSV)