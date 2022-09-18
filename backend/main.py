import json
import requests
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

APIKEY= "62d08a952c7f8f4363cb0b55bdfd43830cb1a851205de2ca7a107bbf3c21cdbd"

# ----------- FAST API -----------------
app = FastAPI()
# -------- Fix cross origin problems -------
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
class URL(BaseModel):
    id: int
    scan_url: list

def getScanResult(input: URL):
    id = base64.urlsafe_b64encode(input.scan_url.encode()).decode().strip("=")
    print("-----------------Report------------")
    url_4Report = f"https://www.virustotal.com/api/v3/urls/{id}"
    header_4Report = {"accept": "application/json","x-apikey":APIKEY}
    response = requests.get(url=url_4Report, headers=header_4Report)
    print(response.text)
    return {"Method":"GET","status": "SUCCESS", "data":response.text}


@app.post("/scanURL")
def scanURL(input: URL):
    url = "https://www.virustotal.com/api/v3/urls"
    payload = f"url={input.scan_url}"
    headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey":APIKEY
    }
    response = requests.post(url,data=payload, headers=headers)
    print(response.text)
    return {"Method":"POST","status": "SUCCESS", "data":response.text}



