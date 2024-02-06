from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Property,
    PropertyImage,
    PropertySpecification,
    PropertySpecificationValue,
    PropertyType,
)

admin.site.register(Category, MPTTModelAdmin)


class PropertySpecificationInline(admin.TabularInline):
    model = PropertySpecification


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    inlines = [
        PropertySpecificationInline,
    ]


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


class PropertySpecificationValueInline(admin.TabularInline):
    model = PropertySpecificationValue


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [
        PropertySpecificationValueInline,
        PropertyImageInline,
    ]
