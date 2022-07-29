# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:01:36 2022

@author: Sayed
"""

from agora_token_builder import RtcTokenBuilder
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
import uvicorn

class HttpError(BaseModel):
    detail:str
    
    class config:
        scheme_extra = {
            'example':{'detail':'Exception Details.'}
            }
    
class TokenResponse(BaseModel):
    success:bool = True
    token:str


    

class TokenData(BaseModel):
    appID: str
    appCertificate: str
    channelName: str
    userAccount: str
    role: int 
    privilegeExpireTs: float
     

def getToken(data: TokenData):    
    print("Data: ",data.appID)
    token = RtcTokenBuilder.buildTokenWithAccount(data.appID,data.appCertificate,data.channelName,data.userAccount,
    data.role,data.privilegeExpireTs)
    return token
    

def formatResponse(token):
    if(len(token) == 0):
        return TokenResponse(success = False,token='')
    else:
        return TokenResponse(success=True,token=token)
        
    
def generateFinalToken(data: TokenData):
    token = getToken(data)
    return formatResponse(token)
    

    
description = """

# AgoraTokenGeneratorAPI

"""    

app = FastAPI(title = 'AgoraTokenGeneratorAPI',
              description = description,
              version= "0.0.1",
              terms_of_service='', 
              contact={
                  'name':'Sayed', 'url':'', 'email':'phenomenalboy0@gmail.com',
                  },
              license_info={
                  'name':'Apache 2.0',
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                  },
              openapi_tags=[]
              )

    
@app.get('/')
async def root():
    return ""    
    
    
@app.get("/getToken/",
         responses={
    200:{'response':TokenResponse,
         'description':'success',
         },
    400: {
        'response':HttpError,
        'description': 'Error'
        }
    },
    tags=[]) 

async def getMyToken(query: TokenData = Depends()):
    
    try:
        return generateFinalToken(query)
    except Exception as e:
        print(e)
        raise HTTPException(400,detail=str(e))
        

'''
if __name__ == "__main__":  
    uvicorn.run("agoraTokenGenerator:app", host="127.0.0.1", port=5500, log_level="info", reload=True, debug=True, workers=3)
'''


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    