from django.contrib import admin
from catalog.models import *

admin.site.register(Order)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(ItemInOrder)
admin.site.register(Product)

