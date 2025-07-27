from src.permission.service import PermissionCRUD
from fastapi import Depends, HTTPException, status

from src.users.models import User
from src.users.utils import get_current_user


async def has_permission(resource: str, role: str):
    permission = await PermissionCRUD.get_permission_by_pair(role, resource)
    return permission.is_allowed if permission else False


def permission_required(resource: str):
    async def checker(current_user: User = Depends(get_current_user)):
        if not await has_permission(resource, current_user.role):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Доступ отклонен"
            )
        return current_user
    return Depends(checker)
