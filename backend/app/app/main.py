from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router


app=FastAPI(title="SafeCrowd AI API",version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_header=["*"],
)

app.include_router(api_router,prefix="/api/v1")

@app.get("/")
def root():
    return {"message":"SafeCrowd backend is running"}




