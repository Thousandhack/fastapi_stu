from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # 下面两句是表示Item表与User表外键关联
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


"""
SQLAlchemy风格和Pydantic风格
请注意，SQLAlchemy 模型 使用定义属性 = ，并将类型作为参数传递给 Column ，例如：
    name = Column(String)
而Pydantic 模型使用 声明类型 : ，新的类型注释语法/类型提示：
    name: str
"""

