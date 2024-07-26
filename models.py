from sqlalchemy import Column, Integer, String, Boolean

from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    group_id = Column(String, index=True)

class Diary(Base):
    __tablename__ = "diarys"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(String)