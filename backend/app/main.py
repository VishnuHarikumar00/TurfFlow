from fastapi import FastAPI

app = FastAPI(title="TurfFlow API")

@app.get("/")
def root():
    return {"message": "Welcome to TurfFlow"}