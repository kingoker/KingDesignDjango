from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Author, Project, ProjectShots, PhoneNumber

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
    list_display_links = ("title", )


@admin.register(ProjectShots)
class ProjectShotsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_image", "project")
    list_display_links = ("title",)

    def get_image(self, obj):
        return mark_safe(f' <img src={obj.image.url} width="50" height="50" >')

    get_image.short_description = "Изображение"


class ProjectShotsInline(admin.TabularInline):
    model = ProjectShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f' <img src={obj.image.url} width="70" height="70" >')

    get_image.short_description = "Изображение"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date", "get_image", "publicate",)
    list_display_links = ("title",)
    list_filter = ("created_date",)
    list_editable = ("publicate",)
    search_fields = ("title", "category__title")
    inlines = [ProjectShotsInline]
    actions = ["unpublish", "publish"]
    save_on_top = True
    save_as = True
    form = ProjectAdminForm

    def get_image(self, obj):
        return mark_safe(f' <img src={obj.preview.url} width="50" height="50" >')

    get_image.short_description = "Изображение"

    # Снять с публикации
    def unpublish(self, request, queryset):
        row_update = queryset.update(publicate=False)
        if row_update == 1:
            message_bit = "1 Запись была обновлена"
        else:
            message_bit = f"{row_update} записей было обновлено"
        self.message_user(request, f"{message_bit}")

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    # Опубликовать
    def publish(self, request, queryset):
        row_update = queryset.update(publicate=True)
        if row_update == 1:
            message_bit = "1 Запись была обновлена"
        else:
            message_bit = f"{row_update} записи было обновлено"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image",)
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f' <img src={obj.photo.url} width="40" height="50" >')

    get_image.short_description = "Изображение"


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("number", "date")
    list_display_links = ("number",)
    list_filter = ("number",)


admin.site.site_title = "KingDesign"
admin.site.site_header = "KingDesign"

