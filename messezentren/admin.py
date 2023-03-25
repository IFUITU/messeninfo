from django.contrib import admin
from .models import messezentren

# Register your models here.


class messezentrenClass(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (

                ('firma', 'firma_en', 'firma_fr', 'firma_es', 'firma_ru', 'firma_cn', 'synono', 'freim2', 'gesamtm2', 'hallenazahl', 'strasse', 'text_en', 'text_de','text_fr', 'text_es', 'text_ru', 'text_cn', 'lat', 'lon', 'ort', 'plz', 'tel', 'fax', 'url', 'land_id', 'email', 'angelegt', 'hallenm2','parkplatzan','flug1','flug2','flug3','flug4','flug5','flug6','flug7','verkehr1','verkehr2', 'verkehr3', 'verkehr4', 'verkehr5', 'anfahrt_de', 'anfahrt_en', 'anfahrt_fr', 'anfahrt_es', 'anfahrt_cn', 'anfahrt_ru')
            ),
        }),
    )
    


admin.site.register(messezentren, messezentrenClass)
