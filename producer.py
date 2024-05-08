from fastapi import FastAPI
from envs import *
from pikaConnection import publishMessage

app = FastAPI()

@app.get("/publish/{name}")
async def publish_message(name: str):
    print(f'Publicando cola: {name}')
    publishMessage(name)
    return {"message": name}
