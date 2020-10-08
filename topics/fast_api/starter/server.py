from fastapi import FastAPI
from fastapi import UploadFile, File
from starlette.responses import RedirectResponse
import uvicorn

from prediction import read_image, predict, load_model

count = 0

app = FastAPI()

@app.get('/index')
def hello_world(name: str):
    return f"Hello {name}!"

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    
    load_model()
    image = read_image(await file.read())
    prediction = predict(image)

    return prediction

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0', debug=True)
