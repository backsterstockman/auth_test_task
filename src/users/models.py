from src.db import Base, intpk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, String


class User(Base):
    __tablename__ = 'users'
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    surname: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[Boolean] = mapped_column(Boolean, server_default='true')
    role: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default='user')

    resumes: Mapped[list['Resume']] = relationship( # type: ignore # noqa
        'Resume',
        back_populates='user'
    )
