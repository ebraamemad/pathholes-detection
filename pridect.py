from ultralytics import YOLO
from PIL import Image
import numpy as np

tuned_mopdel_path =YOLO(r"runs/detect/train/weights/best.pt")

def predict(image_path):
    # Load the image
    results = tuned_mopdel_path.predict(image_path)
    
    results = results[0]  # Get the first result
    image_path = results.plot()  # Plot the results on the image
    pilled_image = Image.fromarray(image_path)  # Convert the result to a PIL image
    
    return pilled_image

# Example usage
if __name__ == "__main__":
    image_path = r"potholes-detect-1\train\images\3_jpg.rf.d13e50350a791c19b898d1c8f3bba78e.jpg"  # Replace with your image path
    predicted_image = predict(image_path)
    predicted_image.show()  # Display the predicted image
    predicted_image.save("predicted_image.jpg")  # Save the predicted image