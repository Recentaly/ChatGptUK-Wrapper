# ChatGptUK-Wrapper

Welcome to **ChatGptUK-Wrapper**, a powerful Flask server that allows you to interact with OpenAI models, including GPT-3.5, GPT-3.5-16K, and even the cutting-edge GPT-4. This versatile wrapper can run locally on your PC or be globally accessible.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python
- Flask
- Flask-CORS
- Flask-Cloudflared (if you want global access)
- Fake-Useragent

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ChatGptUK-Wrapper.git
   ```

2. Navigate to the project folder:

   ```bash
   cd ChatGptUK-Wrapper
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The server reads its configuration from the `assets/config.json` file. You can customize parameters such as host, port, and global access in this file.

```json
{
    "host": "0.0.0.0",
    "port": 5000,
    "debug": false,
    "global": true
}
```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Access the server at [http://localhost:5000](http://localhost:5000) (adjust the URL based on your configuration).

## API Endpoints

### 1. `/chat/completions` (POST)

- **Description:** Main route for chat completions.
- **Parameters:**
  - `messages`: List of dictionaries containing messages.
  - `model`: The OpenAI model to use.
  - `temperature`: Temperature for response generation.
  - `presence_penalty`: Presence penalty for response generation.
  - `frequency_penalty`: Frequency penalty for response generation.
  - `top_p`: Top-p parameter for response generation.
  - `stream`: Enable streaming (optional).
- **Response:** Non-streamed or streamed completion based on the request.

### 2. `/models` (GET)

- **Description:** Get a list of available OpenAI models.
- **Response:** JSON array of model IDs.

### 3. `/` (GET)

- **Description:** Root route to check if the server is running.
- **Response:** "Server is running" message.

## Examples

### 1. Chat Completion (Non-Streamed)

```python
import requests

url = "http://localhost:5000/chat/completions"
data = {
    "messages": [{"role": "user", "content": "Hello, ChatGptUK-Wrapper!"}],
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "presence_penalty": 0.5,
    "frequency_penalty": 0.5,
    "top_p": 1.0,
    "stream": False
}

response = requests.post(url, json=data)
print(response.json())
```

### 2. Chat Completion (Streamed) - Example Script

**example.py**

```python
from assets.src.api import API

# Create an instance of the API
Api = API()

# Define a set of messages for the conversation
messages = [
    {"role": "system", "content": "You are GPT-4. The most advanced chatbot in the world. You have web search capabilities, calculator, and web browser. You can also do translations, and much more."},
    {"role": "user", "content": "Hi, what's the weather like in Washington DC?"},
]

# Stream responses from the API
for chunk in Api.chat(
    messages=messages,
    model="gpt-4-1106-preview",
    temperature=1,
):
    # Print each chunk as it arrives
    print(chunk, end="", flush=True)

# Expected Output: Gradually, words appear as the model processes the input.
```

This example showcases the flexibility of the ChatGptUK-Wrapper API to stream responses in real-time. Adjust the `messages`, `model`, and other parameters according to your specific use case. Feel free to experiment and integrate this functionality into your applications.
