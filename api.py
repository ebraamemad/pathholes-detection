from pridect import predict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
from pydantic import BaseModel
import io

app = FastAPI()


@app.post("/predict/")
async def predict_img(file: UploadFile = File(...)):
    
    Image= Image.open(file.file)
    
    predicted_image = predict(Image)
    Buffer = io.BytesIO()
    predict_img.save(Buffer,format="png")
    Buffer.seek(0)
    
    return StreamingResponse(Buffer, media_type="image/png")