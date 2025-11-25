import asyncio
from agent_framework import ChatAgent
from dotenv import load_dotenv

load_dotenv()

async def main():
    agent = ChatAgent(
        instructions="You are a helpful assistant that keeps track of my day",
        name="Assistant",
        model="gemini-flash-latest"
    )
    
    print(f"Running agent {agent.name}...")
    result = await agent.run("My name is Ahmad Masood")
    print("Agent reply:", result.text)

    result = await agent.run("What is my name?")
    print("Agent reply:", result.text)

    print("Streaming reply:")
    async for chunk in agent.run_stream("Tell me a short story about a brave knight."):
        if chunk:
            print(chunk, end="", flush=True)
    print() # Newline at the end

if __name__ == "__main__":
    asyncio.run(main())