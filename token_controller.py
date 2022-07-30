from pydantic import BaseModel
from agora_token_builder import RtcTokenBuilder
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException


class TokenData(BaseModel):
    appID: str
    appCertificate: str
    channelName: str
    role: str 
    privilegeExpireTs: str


def getToken(data: TokenData):
    token = RtcTokenBuilder.buildTokenWithAccount(data.appID,data.appCertificate,data.channelName,'El Sayed',
    int(data.role),float(data.privilegeExpireTs))
    return token

