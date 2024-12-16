from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List  # Import List from typing
from generator import TextImageGenerator  # Assuming your generator is in a module named generator

app = FastAPI()

# Define the data model with a list of image URLs or filenames
class ImageList(BaseModel):
    image_list: List[str]  # A list of strings (image URLs or filenames)

# Allow CORS for your frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def image_generate(list_of_images: ImageList):
    # Call the image generation function with the list of words
    final_list = TextImageGenerator().generate_and_save_images(list_of_images.image_list)
    
    # Return the filenames as part of the response
    return {"status": "Images generated", "image_list": final_list}

