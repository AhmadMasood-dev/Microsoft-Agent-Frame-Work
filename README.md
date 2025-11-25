# Microsoft Agent Framework (Gemini Edition)

This project is a custom implementation of an agent framework using Google's **Gemini API**. It mimics the structure of the Microsoft Agent Framework but uses Gemini for intelligence.

## What We've Built So Far

1.  **Agent Framework**: A local package (`agent_framework`) that wraps the Gemini SDK.
2.  **Memory**: The agent remembers your name and context during the conversation.
3.  **Streaming**: The agent can "type out" answers in real-time (streaming) instead of waiting for the whole response.

## How to Run It

### 1. Prerequisites

You need to have Python installed.

### 2. Setup

First, make sure you have your virtual environment set up and dependencies installed:

```bash
# Install dependencies (if you haven't already)
.venv/bin/pip install google-generativeai python-dotenv
```

### 3. Configure API Key

Make sure you have a `.env` file in the root directory with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Agent

Run the main script to see the agent in action:

```bash
.venv/bin/python mainAgent.py
```

## Project Structure

- `mainAgent.py`: The entry point. This is where you talk to the agent.
- `agent_framework/`: The "engine" of the project.
  - `agent.py`: Contains the `ChatAgent` class that handles the Gemini connection, memory, and streaming.
- `.env`: Stores your secret API key.
