from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, BigInteger
from sqlalchemy.sql import func
from enum import Enum as EnumBase

from .base import Base, CRUDMixin


class UserType(EnumBase):
    private = "private"
    group = "group"
    supergroup = "supergroup"
    channel = "channel"


class User(Base, CRUDMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    chat_id = Column(BigInteger, unique=True, nullable=False)
    chat_type = Column(Enum(UserType, name="user_type_enum"), nullable=False)
    language_code = Column(String(10), nullable=True)
    group_title = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)

    is_active = Column(Boolean, server_default='1', nullable=False)
    is_admin = Column(Boolean, server_default='0', nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
