from pydantic import BaseModel


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "Exception Details."},
        }


class generatedTokenResponse(BaseModel):
    token: str = ''