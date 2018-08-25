from django.shortcuts import render

from archivist.common.models import MediaItem
from archivist.common.tables import MediaItemTable


def index(request):
    mediaItems = MediaItem.objects.all()
    miTable = MediaItemTable(mediaItems)
    context = {
        "mediaItemTable": miTable,
    }
    return render(request, 'common/index.html', context)
