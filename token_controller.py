from pydantic import BaseModel
from agora_token_builder import RtcTokenBuilder
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException


class TokenData(BaseModel):
    appID: str
    appCertificate: str
    channelName: str
    role: int 
    privilegeExpireTs: float


def getToken(data: TokenData):
    token = RtcTokenBuilder.buildTokenWithAccount(data.appID,data.appCertificate,data.channelName,'El Sayed',
    data.role,data.privilegeExpireTs)
    return token

