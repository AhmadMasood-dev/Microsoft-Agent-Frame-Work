import os
import google.generativeai as genai
from dataclasses import dataclass

@dataclass
class Response:
    text: str

class ChatAgent:
    def __init__(self, instructions: str, name: str, model: str = "gemini-flash-latest"):
        self.instructions = instructions
        self.name = name
        self.model_name = model
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            self.model_name,
            system_instruction=instructions
        )
        self.chat = self.model.start_chat(history=[])

    async def run(self, message: str) -> Response:
        try:
            # Use the chat session to send messages
            response = self.chat.send_message(message)
            return Response(text=response.text)
        except Exception as e:
            return Response(text=f"Error: {str(e)}")

    async def run_stream(self, message: str):
        try:
            response = self.chat.send_message(message, stream=True)
            for chunk in response:
                yield chunk.text
        except Exception as e:
            yield f"Error: {str(e)}"
