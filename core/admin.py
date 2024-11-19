from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Core,Author,Description,Tags
admin.site.site_header = 'Mysite Admin'
admin.site.site_title = 'Mysite '


class CoreAddVersion(admin.StackedInline):
    model = Core
    extra = 1

class CoreAdmin(admin.ModelAdmin):
    list_display = ('title','author'  , 'core_types' ,'get_cover_image' , 'is_check','content','created','updated')
    list_filter = ('author' , 'core_types')
    list_editable =  ('core_types',) 
    search_fields =('title','content')
    readonly_fields = ('created','updated')
    # autocomplete_fields = ('author')

    fieldsets = (
        ('Blog Information ' , {
            'fields': ('title' , 'author' ,'core_types','is_check','content')
        }),
        ( 'Date Information ' , {
            'fields': ('created' , 'updated',)
        }

        )

    )




    def  get_cover_image(self,obj):
        if obj.cover_image:
            img = '<img src ="{url}" width="200px" />'.format(url=obj.cover_image.url)
            return format_html(img)
        return format_html ('<p style = "color:red">No Image</p>')
    get_cover_image.short_description = 'Cover Image'


class TagsAdmin(admin.ModelAdmin):
    search_fields = ('author',)



admin.site.register(Core ,CoreAdmin)
admin.site.register(Author )
admin.site.register(Description)
admin.site.register(Tags , TagsAdmin)
