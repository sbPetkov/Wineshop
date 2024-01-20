from django.contrib import admin

from shop.models import Category, Wine, Customer, Orders


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'password')


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'shipping_address', 'order_date', 'display_items', 'quantity')

    def display_items(self, obj):
        return ', '.join([wine.title for wine in obj.items.all()])

    display_items.short_description = 'Items'
