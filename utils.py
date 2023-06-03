import xmltodict
from datetime import datetime
from urllib.request import Request, urlopen


def unix(stamp: str) -> int:
    return int(datetime.fromisoformat(stamp).timestamp())


def feed(channel_id: str) -> dict:
    req = Request(
        f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}", 
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        },
        method='GET'
    )
    xml_data = urlopen(req).read()
    data = xmltodict.parse(xml_data)['feed']
    channel_name = data['title']
    channel_id = data['yt:channelId']
    current_video = data['entry'][0]
    video_id = current_video['yt:videoId']
    video_title = current_video['title']
    video_published = current_video['published']
    return {
        'channel_name': channel_name,
        'channel_id': channel_id,
        'video_id': video_id,
        'video_title': video_title,
        'video_url': f'https://youtu.be/{video_id}',
        'video_published': str(unix(video_published)),
    }
