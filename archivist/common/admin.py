from django.contrib import admin


from archivist.common.models import MediaItem, MediaInformation

admin.site.register(MediaItem)
admin.site.register(MediaInformation)
