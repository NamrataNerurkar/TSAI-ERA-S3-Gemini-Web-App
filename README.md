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

## LLM Integration

The app is now integrated with **Gemini 2.0 Flash** for real AI responses!

### Setup Gemini API:

1. **Get API Key**:
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key

2. **Configure Environment**:
   - Create a `.env` file in the project root
   - Add your API key: `GEMINI_API_KEY=your_api_key_here`

3. **Run the App**:
   ```bash
   uv run main.py
   ```

### Fallback System:
- If Gemini API fails or is unavailable, the app automatically falls back to intelligent mock responses
- This ensures the app always works, even without internet or API access

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
