import xmltodict
from urllib.request import urlopen


def feed(channel_id: str) -> dict:
    xml_data = urlopen(f'https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}').read()
    data = xmltodict.parse(xml_data)['feed']
    channel_name = data['title']
    channel_id = data['yt:channelId']
    current_video = data['entry'][0]
    video_id = current_video['yt:videoId']
    video_title = current_video['title']
    video_url = current_video['link']['@href']
    video_published = current_video['published']
    return {
        'channel_name': channel_name,
        'channel_id': channel_id,
        'video_id': video_id,
        'video_title': video_title,
        'video_url': video_url,
        'video_published': video_published
    }


if __name__ == '__main__':
    print(feed('UCZHDG3CPvor560dYeOZAv9Q'))