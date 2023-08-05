from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['auction', 'id', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ('Общее', {'fields': ('title', 'description')}),
        ('Финансы', {'fields': ('price', 'auction')}),
    )


admin.site.register(Advertisements, AdvertisementAdmin)
# Register your models here.
