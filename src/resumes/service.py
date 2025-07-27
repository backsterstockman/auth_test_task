from src.resumes.models import Resume
from src.db import BaseCRUD


class ResumeCRUD(BaseCRUD):
    model = Resume
