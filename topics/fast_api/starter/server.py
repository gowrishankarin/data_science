from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn

from prediction import read_image, preprocess, predict

app = FastAPI()

@app.get('/index')
def hello_world(name: str):
    return f"Hello {name}!"

@app.post('/api/predict')
async def predict(file: UploadFile=File(...)):
    extension = file.filename.split('.')[-1] in ("jpg", "jpeg", "png")
    
    if not extension:
        return "Image format not supported"
    
    
    
    # Step 1: Read the file uploaded by the user
    image = read_image(await file.read())
    # Step 2: Preprocess the images
    image = preprocess(image)
    # Step 3: Make predictions/detections
    predictions = predict(image)
    print(predictions)
    
    return predictions

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0', debug=True)
