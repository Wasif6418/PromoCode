
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('suggestions',)


admin.site.register(Product, ProductAdmin)

"""

from django.contrib import admin
from .models import Product, Suggestion


class SuggestionInline(admin.TabularInline):
    model = Suggestion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [SuggestionInline]


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    pass



"""