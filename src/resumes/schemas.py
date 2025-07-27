from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    job_time: str
    salary: int | None
    about_me: str | None
    user_id: int
