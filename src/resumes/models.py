from src.db import Base, intpk
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class JobTime(Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class Resume(Base):
    __tablename__ = 'resumes'
    id: Mapped[intpk]
    job_time: Mapped[JobTime]
    salary: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )
    about_me: Mapped[str] = mapped_column(
        String(200),
        nullable=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )

    user: Mapped['User'] = relationship( # type: ignore # noqa
        'User',
        back_populates='resumes'
    )
