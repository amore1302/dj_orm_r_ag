from django.contrib import admin
from .models import Flat, Claim
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    readonly_fields = ["created_at"]
    raw_id_fields = ('liked_by',)

class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('own_flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)





