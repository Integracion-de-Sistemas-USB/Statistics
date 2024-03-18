from fastapi import FastAPI

import router

app = FastAPI()

@app.get("/") 
def read_root(): 
    return {"Hello" : "World"}

app.include_router(router.router)