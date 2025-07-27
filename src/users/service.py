from sqlalchemy import select
from src.resumes.models import Resume
from src.db import BaseCRUD, async_session_maker
from src.users.models import User


class UserCRUD(BaseCRUD):
    model = User

    @staticmethod
    async def get_user_by_email(email):
        async with async_session_maker() as session:
            result = await session.execute(
                select(User).where(User.email == email)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def get_resumes_by_user_id(user_id: int):
        async with async_session_maker() as session:
            result = await session.execute(
                select(Resume).where(Resume.user_id == user_id)
            )
            return result.scalars().all()
