from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return 'hello17'

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
