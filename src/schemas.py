from pydantic import BaseModel

class GigaTokenManangerSchema(BaseModel):
    access_token: str
    expires_at: int