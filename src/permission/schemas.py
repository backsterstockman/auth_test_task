from pydantic import BaseModel


class PermissionResponse(BaseModel):
    role: str
    resource: str
    is_allowed: bool
