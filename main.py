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
            data = channel.info
            upload = channel.recent_uploaded
            stream = channel.livestream
            if upload:
                data['latest'] = {'id': upload.id, 'url': upload.url}
            if stream:
                data['stream'] = {'id': stream.id, 'url': stream.url}
        except Exception as e:
            return JSONResponse({'error': str(e)}, status_code=404)
        else:
            return JSONResponse(data, status_code=200)
    return JSONResponse({'error': 'channel_id is required'}, status_code=400)
