from django.contrib import admin
from django.utils.html import format_html

from network.models import Seller, Product, Contact





@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "type",
        "contact",
        "contact",
        "product",
        "supplier_link",
        "debt",
        "created_time",
    )
    actions = ("remove_debt",)

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/seller/{obj.supplier.id}/change/"
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"

    @admin.action(description="Удаление задолженности")
    def remove_debt(modeladmin, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "model",
        "date",
    )
    list_filter = ("name",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "email",
        "country",
        "city",
        "street",
        "building",
    )
    list_filter = ("city",)
