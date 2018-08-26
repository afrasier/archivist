from archivist.common.models import MediaItem

import django_tables2 as tables


class MediaItemTable(tables.Table):
    class Meta:
        model = MediaItem
        template_name = 'django_tables2/bootstrap.html'
