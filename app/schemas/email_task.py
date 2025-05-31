from pydantic import BaseModel, field_validator, EmailStr
from datetime import datetime, timezone
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
                d = datetime.fromisoformat(v)
            except ValueError:
                raise ValueError("Invalid datetime format. Use ISO 8601.")

            if d.tzinfo is None:
                raise ValueError(
                    "Scheduled time must include a timezone (e.g., +05:30)"
                )

            d_utc = d.astimezone(timezone.utc)

            if d_utc <= datetime.now(timezone.utc):
                raise ValueError("Scheduled time must be in the future")

            return d_utc

        raise ValueError("Scheduled time must be a valid ISO 8601 datetime string")


class EmailTaskResponse(BaseModel):
    id: uuid.UUID
    email_from: EmailStr
    email_to: EmailStr
    subject: str
    body: str
    status: str
    send_at: datetime  # HH:MM DD-MM-YYYY format
    sent_at: str | None = None
    retry_count: int = 0
    error_message: str | None = None

    class Config:
        from_attributes = True
