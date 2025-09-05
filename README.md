# CNN Learning Assistant

An AI-powered web application that provides personalized teaching about Convolutional Neural Networks (CNNs) based on your learning level and specific questions.

## Features

- **Adaptive Learning**: Choose your learning level (Beginner, Intermediate, or Advanced)
- **Interactive Interface**: Ask specific questions about CNNs
- **AI-Powered Responses**: Get tailored explanations based on your expertise level
- **Beautiful UI**: Modern, responsive design with attractive colors and animations
- **Local LLM Integration**: Ready to work with local LLM setups like Ollama

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Open Your Browser**:
   Visit `http://localhost:8000` to start learning!

## How It Works

1. **Select Your Learning Level**: Choose from three options based on your CNN knowledge
2. **Ask Your Question**: Type any question about CNNs in the text area
3. **Get Personalized Answer**: Receive a tailored response that matches your learning level

## Local LLM Integration

The app is designed to work with local LLMs. Currently, it includes mock responses for demonstration. To integrate with a real local LLM:

1. **Ollama Setup** (recommended):
   - Install Ollama: https://ollama.ai/
   - Pull a model: `ollama pull llama2`
   - Uncomment the Ollama code in `main.py`

2. **Other Options**:
   - LM Studio
   - Local transformers models
   - Custom LLM APIs

## Project Structure

```
cnn-trainer-app/
├── main.py              # FastAPI backend
├── templates/
│   └── index.html       # Frontend HTML with embedded CSS/JS
├── system_prompt.txt    # AI teaching prompt template
├── pyproject.toml       # Dependencies
└── README.md           # This file
```

## Customization

- **System Prompt**: Edit `system_prompt.txt` to modify the AI's teaching style
- **Styling**: Modify the CSS in `templates/index.html` to change the appearance
- **LLM Integration**: Update the `call_local_llm()` function in `main.py`

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- Jinja2
- Requests

## License

MIT License
