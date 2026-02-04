from typing import Union
from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

GITHUB_STATUS_URL = "https://www.githubstatus.com/api/v2/status.json"

class StatusInfo(BaseModel):
    indicator: str
    description: str

class StatusResponse(BaseModel):
    status: StatusInfo
    page: dict

@app.get("/github-status", response_model=StatusResponse)
def read_github_status():
    response = requests.get(GITHUB_STATUS_URL)
    return response.json()


