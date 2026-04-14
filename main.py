from fastapi import FastAPI


app = FastAPI(title="FastAPI Git Workflow")



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Git Demo!"}