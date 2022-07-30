# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:01:36 2022

@author: Sayed
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
import uvicorn
import response_controller
import  token_controller

description = "# AgoraTokenGeneratorAPI 🚀"

tags_metadata = [
    {
        "name":"getToken",
        "description":"Token Genrator"
    }
]
   
app = FastAPI(
    title="AgoraTokenGenerator",
    description=description,
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "Sayed",
        "url": "http://www.example.com/contact/",
        "email": "phenomenalboy0@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

@app.get("/")
async def root():
    return "Main Home"



@app.get("/getToken/",
         responses={
             200: {"token": response_controller.generatedTokenResponse, "description": "Success", },
             400: {
                 "token": response_controller.HTTPError,
                 "description": "Error",
             },
         },
         tags=["getToken"])
async def getMyToken(query: token_controller.TokenData = Depends()):
    try:
        return token_controller.getToken(query)
    except Exception as e:
        print(e)
        raise HTTPException(400, detail=str(e))

'''
if __name__ == "__main__":  
    uvicorn.run("agoraTokenGenerator:app", host="127.0.0.1", port=5500, log_level="info", reload=True, debug=True, workers=3)
'''


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    