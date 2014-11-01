from django.contrib import admin


from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'order', 'album', 'player', 'es_pharrel')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    list_editable = ('title', )
    raw_id_fields = ('artist', )

    def es_pharrel(self, obj):
        return obj.id == 1

    es_pharrel.boolean = True

admin.site.register(Track, TrackAdmin)
