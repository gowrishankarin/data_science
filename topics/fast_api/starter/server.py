from fastapi import FastAPI
from fastapi import UploadFile, File
from starlette.responses import RedirectResponse
import uvicorn

from prediction import read_image, preprocess, predict

count = 0

app = FastAPI()

@app.get('/index')
def hello_world(name: str):
    return f"Hello {name}!"

@app.post('/api/predict')
async def predict(file: UploadFile=File(...)):
    global count
    
    count += 1
    
    extension = file.filename.split('.')[-1] in ("jpg", "jpeg", "png")
    print(f'Extension {count}: {file.filename.split(".")[-1]}')
#     if not extension:
#         return "Image format not supported"
    
    # Step 1: Read the file uploaded by the user
    image = await file.read()
    image = read_image(image)
    
    print(f'Image: {image}')
    # Step 3: Make predictions/detections
    predictions = predict(image)
    print(predictions)
    
    return predictions

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0', debug=True)
