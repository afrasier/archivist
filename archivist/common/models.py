from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

from django.core.validators import MinValueValidator, MaxValueValidator

from djchoices import DjangoChoices, ChoiceItem


class MediaItem(models.Model):
    """
    Represents a media item
    """

    class OwnershipStatus(DjangoChoices):
        """
        Represents the ownership status of a particular media item
        """
        own = ChoiceItem("OWN")
        want = ChoiceItem("WANT")
        research = ChoiceItem("RSCH")
        borrowed = ChoiceItem("BRRW")
        streamed = ChoiceItem("STRM")  # For cataloging media consumed via streaming services

    class CompletionStatus(DjangoChoices):
        """
        Represents the completion status for this entry
        """
        completed = ChoiceItem("CMPT")
        in_progress = ChoiceItem("INPG")
        dropped = ChoiceItem("DRPD")
        in_queue = ChoiceItem("INQU")

    # Model fields defined here

    name = models.CharField(max_length=240, help_text="The name of this media item")
    tags = ArrayField(
        models.CharField(max_length=20, help_text="A tag for a media item")
    )

    ownership_status = models.CharField(
        max_length=4,
        choices=OwnershipStatus.choices,
        help_text="The ownership status of this item"
    )

    completion_status = models.CharField(
        max_length=4,
        choices=CompletionStatus.choices,
        help_text="The completion status of this item"
    )

    rating = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(-1)],
        default=-1
    )

    def __str__(self) -> str:
        return f"{self.name}"


class MediaInformation(models.Model):
    """
    Contains a blob of information about a specific media item, associated via a
    onetoone field from MediaItem.

    This is maintained as a separate model so that all of the JSON blobs are in
    an individual table.
    """

    item = models.OneToOneField(MediaItem,
                                on_delete=models.CASCADE,
                                related_name="metadata",
                                primary_key=True)
    data = JSONField()

    def __str__(self) -> str:
        return f"MediaInformation for MediaItem {self.item}"
