from pydantic import BaseModel, field_validator, EmailStr
from datetime import datetime
import uuid


class EmailTaskCreate(BaseModel):
    email_from: EmailStr
    email_to: EmailStr
    subject: str
    body: str
    send_at: datetime

    @field_validator("send_at", mode="before")
    @classmethod
    def parse_scheduled_time(cls, v):
        if isinstance(v, str):
            try:
                return datetime.strptime(v, "%H:%M %d/%m/%Y")
            except ValueError:
                raise ValueError("Time must be in 'HH:MM DD/MM/YYYY' format")
        elif not isinstance(v, datetime):
            raise ValueError(
                "Scheduled time must be a datetime object or a valid string"
            )
        return v


class EmailTaskResponse(BaseModel):
    id: uuid.UUID
    email_from: EmailStr
    email_to: EmailStr
    subject: str
    body: str
    status: str
    send_at: datetime  # HH:MM DD-MM-YYYY format
    sent_at: str|None = None
    retry_count: int = 0
    error_message: str|None = None

    class Config:
        from_attributes = True
