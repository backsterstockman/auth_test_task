from sqlalchemy import String, UniqueConstraint
from src.db import Base, intpk
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column


class Role(Enum):
    user = "user"
    admin = "admin"


class Resource(Enum):
    users = "users"
    permissions = "permissions"


class Permission(Base):
    __tablename__ = 'permissions'

    id: Mapped[intpk]
    role: Mapped[Role] = mapped_column(String, nullable=False)
    resource: Mapped[Resource] = mapped_column(String, nullable=False)
    is_allowed: Mapped[bool] = mapped_column(nullable=False)

    __table_args__ = (
        UniqueConstraint('role', 'resource', name='unique_permission'),
    )
