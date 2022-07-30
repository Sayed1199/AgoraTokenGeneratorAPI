from pydantic import BaseModel
from agora_token_builder import RtcTokenBuilder
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException


class TokenData(BaseModel):
    appID: str
    appCertificate: str
    channelName: str
    uid:str
    role: str 
    privilegeExpireTs: str


def getToken(data: TokenData):
    token = RtcTokenBuilder.buildTokenWithUid(data.appID,data.appCertificate,data.channelName,int(data.uid),
    int(data.role),float(data.privilegeExpireTs))
    return token

