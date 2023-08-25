from django.contrib import admin
from .models import Advertisements
from django.utils.html import format_html
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'photo']
    list_filter = ['auction', 'id', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    readonly_fields = ['photo']
    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    @admin.display
    def photo(self, obj):
        if Advertisements.image:
            return format_html(f'<img src="{obj.image.url}" width= "55" height = "50">')
        else:
            return format_html(f'<img src="{obj.image.url}" width= "55" height = "50">')
    fieldsets = (
        ('Общее', {'fields': ('title', 'description', 'image')}),
        ('Финансы', {'fields': ('price', 'auction')}),
    )


admin.site.register(Advertisements, AdvertisementAdmin)
# Register your models here.
