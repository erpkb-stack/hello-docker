from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Docker - Testing git Actions !!! Git Action is sucessful now!", "container": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "ok"}
