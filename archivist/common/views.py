from django.shortcuts import render

from django_tables2 import RequestConfig

from archivist.common.models import MediaItem
from archivist.common.tables import MediaItemTable


def index(request):
    mediaItems = MediaItem.objects.all()
    miTable = MediaItemTable(mediaItems)
    RequestConfig(request).configure(miTable)
    context = {
        "mediaItemTable": miTable,
    }
    return render(request, 'common/index.html', context)
