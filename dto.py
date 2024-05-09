from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Student(BaseModel):
    id: str
    name: str
    age: int
    transactionDate: Optional[datetime] = datetime.now()
    