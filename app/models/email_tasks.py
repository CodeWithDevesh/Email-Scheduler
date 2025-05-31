from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID, ENUM
import uuid
from datetime import datetime, timezone
from app.database import base


class EmailStatus(ENUM):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"

class email_tasks(base):
    __tablename__ = "email_tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email_from = Column(String, nullable=False)
    email_to = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    status = Column(EmailStatus, nullable=False, default=EmailStatus.PENDING)

    send_at = Column(DateTime(timezone=True), nullable=False)
    sent_at = Column(DateTime(timezone=True), nullable=True)

    retry_count = Column(Integer, nullable=False, default=0)
    error_message = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))