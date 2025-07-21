from django.contrib import admin
from django.utils.text import slugify

from .models import Element, Type, Category
# Register your models here.
class ElementInline(admin.StackedInline):
    model = Element


@admin.register(Category, Type)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    # inlines = [
    #     ElementInline
    # ]

@admin.display(description='iD and Title uppercase')
def upper_title(obj):
    return f"{obj.id}-{obj.title}".upper()

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','type', upper_title, 'cheap')
    #fields = (('title', 'slug'), 'description', 'price', ('category', 'type'))
    fieldsets = [
        (
            "Regular options",
            {
                "fields": (('title', 'slug'), 'description', ('category', 'type'))
            }
        ),
        (
            "Advanced options",
            {
                "fields": ('price',),
                "classes": ('collapse',)
            }
        )
    ]
    def save_model(self, request, obj, form, change):

        if not(change) and obj.slug == '':
            obj.slug = slugify(obj.title)

        if obj.slug == '':
            obj.slug = slugify(obj.title)

        super().save_model(request, obj, form, change)