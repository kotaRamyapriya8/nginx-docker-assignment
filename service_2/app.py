from fastapi import FastAPI

app = FastAPI()

@app.get("/service2")
def read_root():
    return {"message": "Hello from Service 2"}

