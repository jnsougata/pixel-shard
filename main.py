from utils import feed
from aiotube import Channel
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World"})


@app.get("/ch/{channel_id}")
async def info(channel_id: str = None):
    if channel_id:
        try:
            channel = Channel(channel_id)
            data = channel.metadata
            stream_id = channel.streaming_now()
            upload_id = channel.last_uploaded()
            if upload_id:
                data['upload'] = {'id': upload_id, 'url': f"https://www.youtube.com/watch?v={upload_id}"}
            if stream_id:
                data['live'] = {'id': stream_id, 'url': f"https://www.youtube.com/watch?v={stream_id}"}
        except Exception as e:
            return JSONResponse({'error': str(e)}, status_code=404)
        else:
            return JSONResponse(data, status_code=200)
    return JSONResponse({'error': 'channel_id is required'}, status_code=400)


@app.get("/feed/{channel_id}")
async def serve_feed(channel_id: str):
    try:
        return feed(channel_id)
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=404)
