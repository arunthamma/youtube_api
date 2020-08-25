import json
import time
import logging
import threading
from apiclient.discovery import build
from api.models.youtube_data import YoutubeData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

LOGGER = logging.getLogger()
youtube_api_key = 'AIzaSyAj_uy9a0M5nZ_DDJE2a2WmvXBQnh4ZfMg'
ytRes = build('youtube', 'v3', developerKey=youtube_api_key)
query_string = 'Cricket'

class PollingYT(threading.Thread):
    def __init__(self, **kwargs):
        """
        Initializing threading class for polling youtube data api.
        """
        kwargs['daemon'] = kwargs.get('daemon', True)
        super().__init__(**kwargs)

        self.running = threading.Event()
        self.running.set()
    
    def run(self):
        """
        This is the actual function where youtube data api is called.
        """
        # setting this to 600 as there is a limit of 10000 queries per day
        sleep_time = 600
        while self.running.is_set():
            try:
                search_oper = ytRes.search().list(part='snippet', maxResults=20, type='video', q=query_string)
                result = search_oper.execute()['items']
                for eachItem in result:
                    video_title = eachItem['snippet']['title']
                    video_description = eachItem['snippet']['description']
                    video_tag = eachItem['id']['videoId']
                    channel_tag = eachItem['snippet']['channelId']
                    channel_title = eachItem['snippet']['channelTitle']
                    publish_time = eachItem['snippet']['publishTime']
                    thumbnail = eachItem['snippet']['thumbnails']['default']['url']
                    
                    if YoutubeData.objects.filter(video_tag='video_tag').exists():
                        instance = YoutubeData.objects.get(video_tag='video_tag')
                        # Calling update just in case if the video id doesnt change but the title or thumbnail is updated.
                        instance.update(
                            video_title=video_title,
                            video_description=video_description,
                            publish_time=publish_time,
                            thumbnail=thumbnail
                        )
                    else:
                        YoutubeData.objects.create(
                            video_tag=video_tag,
                            video_title=video_title,
                            video_description=video_description,
                            channel_tag=channel_tag,
                            channel_title=channel_title,
                            publish_time=publish_time,
                            thumbnail=thumbnail
                        )
            except Exception as exp:
                LOGGER.error("Failed to publish video data entries into database. Exception occurred: {}".format(exp))
            time.sleep(sleep_time)

@api_view(['POST'])
def publish_video_data(request):
    """
    This is the django api that gets called only once when the server is fired up.

    Args:
        request (HttpRequest): The HTTP request for this API call.

    Returns:
        None
        Publishes the youtube api data into database
    """
    x = PollingYT()
    # for every 600 seconds this will be running a youtube data api query
    x.start()
    return Response(status=200)


@api_view(['GET'])
def get_video_data(request):
    """
    This returns the list of all YoutubeData objects.

    Args:
        request (HttpRequest): The HTTP request for this API call.

    Returns:
        A serialized list of YoutubeData objects.
    """
    # No youtube api is called here. We just fetch the entries from database.
    all_instances = YoutubeData.objects.all()
    if not all_instances:
        return Response({"message": "No entries found"},
                        status=status.HTTP_204_NO_CONTENT)
    final_list = []
    for instance in all_instances:
        final_list.append({
            'video_title': instance.video_title,
            'video_description': instance.video_description,
            'channel_title': instance.channel_title,
            'thumbnail': instance.thumbnail,
            'video_url': 'http://youtube.com/watch?v={}'.format(instance.video_tag)
        })
    print(final_list)
    return Response(final_list)
        