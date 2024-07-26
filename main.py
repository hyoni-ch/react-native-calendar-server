import uvicorn
from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"hello world!"}



# Read date All , Todo
@app.get("/todos", response_model=list[schemas.Todo])
def read_todos_all(db: Session = Depends(get_db)):
    return crud. get_todos_all(db)

# Read date All , Todo
@app.get("/todo", response_model=list[schemas.Todo])
def read_todos(date: str = Query(None), db: Session = Depends(get_db)):
    return crud.get_todos(db, date)

# Read By GroupId, Todo
@app.get("/todo/{groupId}", response_model=list[schemas.Todo])
def read_todo_one(groupId: str, db: Session = Depends(get_db)):
    return crud.get_todo_one(db, groupId)

# Create , Todo
@app.post("/todo", response_model=schemas.Todo)
def create_todo(item: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, item)

# Update , Todo
@app.put("/todo/{groupId}", response_model=schemas.Todo)
def update_todo(groupId: str, item: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.update_todo(db, groupId, item)

# Delete , Todo
@app.delete("/todo/{groupId}", response_model=schemas.Todo)
def delete_todo(groupId: str, db: Session = Depends(get_db)):
    return crud.delete_todo(db, groupId)




# Read All , Diary
@app.get("/diary", response_model=list[schemas.Diary])
def read_diary_all(db: Session = Depends(get_db)):
    return crud.get_diary_all(db)

# Read date All , Diary
@app.get("/diary/{date}", response_model=list[schemas.Diary])
def read_diary(date: str, db: Session = Depends(get_db)):
    return crud.get_diary(db, date)

# Read One , Diary
@app.get("/diary/{group_id}", response_model=schemas.Diary)
def read_diary_one(groupId: str, db: Session = Depends(get_db)):
    return crud.get_diary_one(db, groupId)

# Create , Diary
@app.post("/diary", response_model=schemas.Diary)
def create_diary(item: schemas.DiaryCreate, db: Session = Depends(get_db)):
    return crud.create_diary(db, item)

# Update , Diary
@app.put("/diary/{group_id}", response_model=schemas.Diary)
def update_diary(groupId: str, item: schemas.DiaryCreate, db: Session = Depends(get_db)):
    return crud.update_diary(db, groupId, item)

# Delete , Diary
@app.delete("/diary/{group_id}", response_model=schemas.Diary)
def delete_diary(groupId: str, db: Session = Depends(get_db)):
    return crud.delete_diary(db, groupId)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)