from pydantic import BaseModel


class TodoBase(BaseModel):
  description: str
  completed: bool = False
  date: str
  start_time: str
  end_time: str
  group_id: str

class TodoCreate(TodoBase):
  pass

class Todo(TodoBase):
  id: int
  
  class Config:
    from_attribute = True


class DiaryBase(BaseModel):
  title: str
  description: str
  date: str


class DiaryCreate(DiaryBase):
  pass

class Diary(DiaryBase):
  id: int

  class Config:
    from_attribute = True