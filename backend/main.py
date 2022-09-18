import json
import requests
import base64
from fastapi import FastAPI

#APIKEY=62d08a952c7f8f4363cb0b55bdfd43830cb1a851205de2ca7a107bbf3c21cdbd

# ----------- FAST API -----------------
app = FastAPI()



@app.get("/")
def getScanResult():
    id = base64.urlsafe_b64encode("www.ntust.edu.tw".encode()).decode().strip("=")
    print("-----------------Report------------")
    url_4Report = f"https://www.virustotal.com/api/v3/urls/{id}"
    header_4Report = {"accept": "application/json","x-apikey":APIKEY}
    response = requests.get(url_4Report, headers=header_4Report)
    print(response.text)
    return {"data":response.text}




# url = "https://www.virustotal.com/api/v3/urls"

# payload = "url=www.google.com"
# headers = {
#     "accept": "application/json",
#     "content-type": "application/x-www-form-urlencoded",
#     "x-apikey":"62d08a952c7f8f4363cb0b55bdfd43830cb1a851205de2ca7a107bbf3c21cdbd"
# }

# response = requests.post(url, data=payload, headers=headers)
# print(response.text)



