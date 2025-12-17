from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base


class Deployment(Base):
    __tablename__ = "deployments"
    id = Column(Integer, primary_key=True, index=True)

    crm_record_id = Column(String, nullable=True)

    scheduled_time = Column(DateTime, nullable=False)
    approval_reminder_time = Column(DateTime, nullable=False)

    approval_status = Column(String, default="pending")
    # pending, approved, rejected

    status = Column(String, default="created")
    # created, running, success, failed

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())