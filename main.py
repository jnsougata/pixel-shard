import fastapi
from aiotube import Channel


app = fastapi.FastAPI()


@app.get("/ch/{id}")
async def info(id: str = None):
    if id:
        channel = Channel(id)
        payload = {
            'latest': {},
            'stream': {},
            'info': channel.info
        }
        upload = channel.recent_uploaded
        if upload:
            latest_url = upload.url
            latest_id = latest_url.split('=')[-1]
            payload['latest'] = {'id': latest_id, 'url': latest_url}

        stream = channel.livestream
        if stream:
            stream_url = stream.url
            stream_id = stream_url.split('=')[-1]
            payload['stream'] = {'id': stream_id, 'url': stream_url}

        return payload
