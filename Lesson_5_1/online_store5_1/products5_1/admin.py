from django.contrib import admin
from .models import *

# 1
@admin.register(Contact) # wrapping function
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'middle_name',
        'prefix_name',
        'company_name',
        'contact_type',
        'address',
        'city',
        'state',
        'country',
        'postal_code',
        'phone',
        'email',
        'create_time'
    ]

# 2
@admin.register(Supplier) # wrapping function
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'contact_id',
        'contract_no',
        'contract_title',
        'supplier_type',
        'contr_eff_date',
        'contr_exp_date',
    ]

# admin.site.register(EmailCollector, EmailCollectorAdmin)