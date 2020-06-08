from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# 如果您使用的是 PostgreSQL 数据库，则只需取消注释以下行：
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # 仅适用于 SQLite 。 其他数据库不需要它
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 要创建 SessionLocal 类，请使用函数 sessionmaker

Base = declarative_base()  # 从该类继承以创建每个数据库模型或类（ORM模型）
