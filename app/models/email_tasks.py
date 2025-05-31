from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID, ENUM
import uuid
from datetime import datetime, timezone
from app.database import Base
import enum


class EmailStatus(enum.Enum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class EmailTasks(Base):
    __tablename__ = "email_tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email_from = Column(String, nullable=False)
    email_to = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    status = Column(
        ENUM(EmailStatus, name="email_status", create_type=True),
        nullable=False,
        default=EmailStatus.PENDING,
    )

    send_at = Column(DateTime(timezone=True), nullable=False)
    sent_at = Column(DateTime(timezone=True), nullable=True)

    retry_count = Column(Integer, nullable=False, default=0)
    error_message = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
