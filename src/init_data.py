from src.users.models import User
from src.resumes.models import Resume
from src.permission.models import Permission
from src.users.service import UserCRUD
from src.resumes.service import ResumeCRUD
from src.permission.service import PermissionCRUD
from src.db import Base, engine
from src.users.utils import hash_password


async def init_db_data():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    user = User(
        name="John",
        surname="Doe",
        email="john.doe@example.com",
        password=hash_password("password"),
        is_active=True,
        role='admin'
    )

    await UserCRUD.create(user)

    resume = Resume(
        user_id=user.id,
        job_time='fulltime',
        salary=1000,
        about_me='Test text'
    )

    await ResumeCRUD.create(resume)

    permissions = [
        Permission(
            resource='/permissions',
            role='admin',
            is_allowed=True
        ),
        Permission(
            resource='/permissions',
            role='user',
            is_allowed=False
        ),
        Permission(
            resource='/users',
            role='admin',
            is_allowed=True
        ),
        Permission(
            resource='/users',
            role='user',
            is_allowed=True
        ),
        # Permission(
        #     resource='/users/resumes',
        #     role='user',
        #     is_allowed=True
        # ),
        # Permission(
        #     resource='/users/resumes',
        #     role='admin',
        #     is_allowed=True
        # ),
        # Permission(
        #     resource='/users/editprofile',
        #     role='admin',
        #     is_allowed=True
        # ),
        # Permission(
        #     resource='/users/editprofile',
        #     role='user',
        #     is_allowed=True
        # ),
        # Permission(
        #     resource='/users/delete',
        #     role='admin',
        #     is_allowed=True
        # ),
        # Permission(
        #     resource='/users/delete',
        #     role='user',
        #     is_allowed=True
        # ),
    ]

    for permission in permissions:
        await PermissionCRUD.create(permission)
