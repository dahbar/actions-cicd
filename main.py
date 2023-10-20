from typing import Union
from fastapi import FastAPI, HTTPException
from models.todo import Todo

app = FastAPI()

todos = []


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/todo/")
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo


@app.get("/todos/")
async def get_todos():
    return todos


@app.get("/todo/{todo_title}/")
async def get_todo(todo_title: str):
    for todo in todos:
        if todo.title == todo_title:
            return todo
    raise HTTPException(status_code=404)


@app.put("/todos/{todo_title}/")
async def update_todo(todo_title: str, new_todo: Todo):
    for todo in todos:
        if todo.title == todo_title:
            todo.title = new_todo.title
            todo.description = new_todo.description
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_title}/")
async def delete_todo(todo_title: str):
    global todos
    todos = [todo for todo in todos if todo.title != todo_title]
    return {"message": "Todo deleted successfully"}
