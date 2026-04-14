from fastapi import FastAPI


app = FastAPI(title="FastAPI Git Workflow")



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Git Demo!"}

# login account
@app.post("/login")
def login(username: str, password: str):
    # Placeholder for login logic
    return {"message": f"Hello, {username}!"}