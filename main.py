import fastapi
from aiotube import Channel


app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"message": Channel('GYROOO').info}
