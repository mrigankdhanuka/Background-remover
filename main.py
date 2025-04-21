from fastapi import FastAPI
import gradio as gr
from gradio_helper import make_demo

app = FastAPI()

# 🔧 Define the on_submit function
def on_submit(image):
    # You can put your background removal logic here
    # For now, just return the same image as a placeholder
    return image

# 🧠 Pass the function to make_demo
demo = make_demo(fn=on_submit)

# 🚀 Mount Gradio onto FastAPI
@app.get("/")
async def root():
    return {"message": "Hello from the FastAPI-Gradio app!"}

# Expose the Gradio app at /gradio
app = gr.mount_gradio_app(app, demo, path="/gradio")
