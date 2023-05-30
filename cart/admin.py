from django.contrib import admin

# Register your models here.

    
from .models import Product, Cart, CartItem

admin.site.register(Product)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['line_total']


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

    readonly_fields = ['total', 'created_at', 'updated_at']

    fields = ['client', 'total', 'created_at', 'updated_at']

    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)
