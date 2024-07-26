from sqlalchemy.orm import Session
import models, schemas

def get_todos_all(db: Session):
    db_items = db.query(models.Todo).order_by(models.Todo.date.desc(), models.Todo.id.desc()).all()
    return db_items

def get_todos(db: Session, date: str):
    db_items = db.query(models.Todo).filter(models.Todo.date == date).order_by(models.Todo.start_time.asc(), models.Todo.end_time.asc(), models.Todo.id.desc()).all()
    return db_items

def get_todo_one(db: Session, groupId: str):
    db_item = db.query(models.Todo).filter(models.Todo.group_id == groupId).order_by(models.Todo.date.desc()).all()
    return db_item

def create_todo(db: Session, item: schemas.TodoCreate):
    db_item = models.Todo(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo(db: Session, groupId: str, item: schemas.TodoCreate):
    db_items = db.query(models.Todo).filter(models.Todo.group_id == groupId).all()

    start_date = item.date
    end_date = item.date
    start_time = item.start_time
    end_time = item.end_time

    for db_item in db_items:
        item_date = db_item.date
        if item_date == start_date:
            db_item.start_time = start_time
        if item_date == end_date:
            db_item.end_time = end_time

        db_item.description = item.description
        db_item.completed = item.completed

    db.commit()
    db.refresh(db_items)
    return db_items

def delete_todo( db: Session, groupId: str):
    db_items = db.query(models.Todo).filter(models.Todo.group_id == groupId).all()
    for item in db_items:
        db.delete(item)
    db.commit()
    return db_items






def get_diary_all(db: Session):
    db_items = db.query(models.Diary).order_by(models.Diary.date.desc(), models.Diary.id.desc()).all()
    return db_items

def get_diary(db: Session, date: str):
    db_items = db.query(models.Diary).filter(models.Diary.date == date).all()
    return db_items

def get_diary_one(db: Session, id: int):
    db_item = db.query(models.Diary).filter(models.Diary.id == id).first()
    return db_item

def create_diary(db: Session, item: schemas.DiaryCreate):
    db_item = models.Diary(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_diary(db: Session, id: int, item: schemas.DiaryCreate):
    db_item = db.query(models.Diary).filter(models.Diary.id == id).one_or_none()
    db_item.description = item.description
    db_item.title = item.title
    db_item.date = item.date
    db.add(db_item)
    db.commit()
    db.flush(db_item)
    return db_item

def delete_diary(db: Session, id: int):
    db_item = db.query(models.Diary).filter(models.Diary.id == id).first()
    db.delete(db_item)
    db.commit()
    return db_item