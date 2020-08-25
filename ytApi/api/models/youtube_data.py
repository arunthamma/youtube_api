from django.db import models

# pylint: disable=too-few-public-methods
class YoutubeData(models.Model):
    """
    YoutubeData class

    Class representing a platform type.
    """
    video_tag = models.CharField(max_length=20, unique=True)
    video_title = models.CharField(max_length=200)
    video_description = models.CharField(max_length=1000)
    channel_tag = models.CharField(max_length=50)
    channel_title = models.CharField(max_length=100)
    publish_time = models.DateTimeField()
    thumbnail = models.URLField()

    class Meta:
        """
        Meta Class

        Metadata for the SvPlatform class.
        """
        db_table = 'youtube_data'
        ordering = ('-publish_time',)
        unique_together = (('video_tag',))
