from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/index')
def hello_world(name: str):
    return f"Hello {name}!"

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
