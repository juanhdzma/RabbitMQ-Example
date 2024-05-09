from fastapi import FastAPI
from envs import *
from pikaConnection import publishMessage
from dto import Student

app = FastAPI()

@app.post("/publish")
async def publish_message(student: Student):
    print(f'Publicando cola: {student}')
    publishMessage(student)
    return student
