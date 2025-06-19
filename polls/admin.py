from django.contrib import admin
from .models import Question

# Register your models here.

admin.site.register(Question)


admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to the Admin Area"
