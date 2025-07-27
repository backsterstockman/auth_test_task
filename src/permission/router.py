from typing import Any
from fastapi.routing import APIRouter
from src.permission.service import PermissionCRUD
from src.permission.schemas import PermissionResponse
from src.users.models import User
from src.utils import permission_required


router = APIRouter(prefix="/permissions")


@router.get('/', response_model=list[PermissionResponse])
async def get_permissions(
    current_user: User = permission_required(router.prefix)
) -> list:
    return await PermissionCRUD().get_all()


@router.patch('/', response_model=PermissionResponse)
async def update_permission(
    resource: str,
    role: str,
    is_allowed: bool,
    current_user: User = permission_required(router.prefix)

) -> Any:

    permission = await PermissionCRUD.get_permission_by_pair(role, resource)

    new_permission = PermissionResponse(
        resource=resource,
        role=role,
        is_allowed=is_allowed
    )

    return await PermissionCRUD().update_by_id(permission.id, new_permission)
