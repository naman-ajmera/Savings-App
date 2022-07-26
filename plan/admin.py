from django.contrib import admin

from plan.models import Plan, Amount, Tenure

# Register your models here.

admin.site.register(Plan)
admin.site.register(Tenure)
admin.site.register(Amount)
