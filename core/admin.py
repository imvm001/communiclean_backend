from django.contrib import admin
from .models import Customer, ServiceBooking, Income, TaxRecord

admin.site.register(Customer)
admin.site.register(ServiceBooking)
admin.site.register(Income)
admin.site.register(TaxRecord)