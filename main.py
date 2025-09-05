from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os
from pathlib import Path
import requests
import json

app = FastAPI(title="CNN Learning Assistant", description="AI-powered CNN tutor")

# Mount static files and templates
templates = Jinja2Templates(directory="templates")

class LearningRequest(BaseModel):
    learning_level: str
    topic_to_learn: str

def load_system_prompt():
    """Load the system prompt from file"""
    prompt_file = Path("system_prompt.txt")
    if prompt_file.exists():
        return prompt_file.read_text()
    else:
        return "Be a very effective, lucid and fun teacher of CNNs to students."

def call_local_llm(prompt: str) -> str:
    """
    Call a local LLM. This is a placeholder implementation.
    You can replace this with your preferred local LLM setup like:
    - Ollama
    - LM Studio
    - Local transformers model
    - etc.
    """
    try:
        # Example using Ollama (uncomment and modify if you have Ollama running)
        # response = requests.post(
        #     "http://localhost:11434/api/generate",
        #     json={
        #         "model": "llama2",  # or your preferred model
        #         "prompt": prompt,
        #         "stream": False
        #     }
        # )
        # return response.json()["response"]
        
        # For now, return a mock response based on the learning level and question
        return generate_mock_response(prompt)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {str(e)}")

def generate_mock_response(prompt: str) -> str:
    """Generate a mock response for demonstration purposes"""
    if "Advanced NN Practitioner" in prompt:
        return """Great question! As an advanced practitioner, you're likely familiar with the core concepts, so let me dive deeper.

CNNs leverage spatial hierarchies through learnable filters that detect increasingly complex patterns. The key insight is that early layers learn low-level features (edges, textures) while deeper layers combine these into high-level semantic representations.

For your specific question, here are some advanced considerations:
- Gradient flow optimization in deep CNNs
- Attention mechanisms in vision transformers
- Efficient architectures like MobileNet or EfficientNet
- Advanced regularization techniques

Would you like me to elaborate on any of these aspects or discuss recent research in this area?"""
    
    elif "Familiar with NNs" in prompt:
        return """Excellent! Since you're familiar with neural networks, let me explain CNNs in that context.

Think of CNNs as specialized neural networks designed for spatial data like images. The key difference is the convolutional layer, which uses filters (kernels) to scan across the image and detect patterns.

Here's how it works:
1. Convolutional layers apply filters to detect features
2. Pooling layers reduce spatial dimensions
3. Fully connected layers make final predictions

The beauty of CNNs is parameter sharing - the same filter is applied across the entire image, making them translation-invariant and much more efficient than fully connected networks for images.

What specific aspect of CNNs would you like to explore further?"""
    
    else:  # Beginner
        return """Welcome to the amazing world of CNNs! Let me explain this in simple terms.

Imagine you're looking at a picture and trying to identify what's in it. CNNs work similarly to how our brain processes visual information!

Here's a simple analogy:
- Think of CNNs like a team of detectives examining a photo
- Each detective looks for specific clues (like edges, shapes, or colors)
- They work together to piece together what the image shows

The "convolutional" part means the network uses small filters that slide across the image, looking for patterns - just like how you might scan a picture with your eyes.

Don't worry if this seems complex - we'll build up your understanding step by step! What would you like to know more about first?"""

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main HTML page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(request: LearningRequest):
    """Process learning request and return AI response"""
    try:
        # Load system prompt
        system_prompt = load_system_prompt()
        
        # Format the prompt with user inputs
        formatted_prompt = system_prompt.format(
            learning_level=request.learning_level,
            topic_to_learn=request.topic_to_learn
        )
        
        # Call the local LLM
        response = call_local_llm(formatted_prompt)
        
        return {"answer": response}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def main():
    """Run the FastAPI application"""
    print("Starting CNN Learning Assistant...")
    print("Visit http://localhost:8000 to use the app")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
