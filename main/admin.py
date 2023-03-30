from django.contrib import admin
from .models import Branchen, Languages, b, Messe, Btom

@admin.register(Languages)
class LangAdmin(admin.ModelAdmin):
    pass

@admin.register(Branchen)
class BranchenAdmin(admin.ModelAdmin):
    list_filter = ("b",)
    # search_fields = ("b_id",)
    # fields = ('b', "text", "beschreibung")


class BranchenInline(admin.TabularInline):
    model = Branchen
    fields = ("sprach", "text", "messe_text", "beschreibung")

@admin.register(b)
class bAdmin(admin.ModelAdmin):
    inlines = [BranchenInline]
    list_display = ['id',]


@admin.register(Messe)
class MesseAdmin(admin.ModelAdmin):
    pass


@admin.register(Btom)
class BtomAdmin(admin.ModelAdmin):
    pass