import json
import string
import requests
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


APIKEY= "62d08a952c7f8f4363cb0b55bdfd43830cb1a851205de2ca7a107bbf3c21cdbd"

app = FastAPI()

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


# class URL(BaseModel):
#     scan_url: str

@app.get("/")

def getScanResult():
    
    id = base64.urlsafe_b64encode('www.google.com'.encode()).decode().strip("=")
    print("-----------------Report------------")
    url_4Report = f"https://www.virustotal.com/api/v3/urls/{id}"
    header_4Report = {"accept": "application/json","x-apikey":APIKEY}
    response = requests.get(url=url_4Report, headers=header_4Report)
    print(response.text)
    return {"Method":"GET","status": "SUCCESS", "data":response.text}



@app.post("/postURL")
def scanURL():
    url = "https://www.virustotal.com/api/v3/urls"
    payload = f"url={input.scan_url}"
    headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "x-apikey":APIKEY
    }
    response = requests.post(url,data=payload, headers=headers)
    print(response.text)
    return {"Method":"POST","status": "SUCCESS", "data":input}

# @app.get("/")
# def get_memes():
#     url = "https://api.imgflip.com/get_memes"
#     header = {"accept": "application/json"}
#     response = requests.get(url=url, headers=header)
#     print(response.text)
#     return {"Method":"GET","status": "SUCCESS", "data":response.text}



