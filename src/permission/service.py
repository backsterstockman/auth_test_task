from src.db import BaseCRUD
from src.permission.models import Permission
from src.db import async_session_maker
from sqlalchemy import select


class PermissionCRUD(BaseCRUD):
    model = Permission

    @staticmethod
    async def get_permission_by_pair(role: str, resource: str):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Permission).where(
                    Permission.role == role,
                    Permission.resource == resource
                )
            )

            permission: Permission = result.scalar_one_or_none()
            return permission
