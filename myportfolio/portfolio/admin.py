from django.contrib import admin

from .models import IntroContent, Project, Image, Tag

admin.site.register(IntroContent)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Tag)

class ImageAdmin(admin.TabularInline):
    model = Image

    # class Meta:
    #     model = Image

class ProjectAdmin(admin.ModelAdmin):

    readonly_fields = ('id',)
    inlines = [
        ImageAdmin
        ]

    class Meta:
        model=Project

