from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
import sys

llm = ChatOpenAI(model="openai/gpt-4o-mini", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
# llm = ChatOpenAI(model="gpt-4o-mini")

async def main():
    # Use command line argument if provided, otherwise use default
    task = sys.argv[1] if len(sys.argv) > 1 else "What is the meaning of life?"
    
    agent = Agent(
        task=task,
        llm=llm,
    )
    await agent.run()

asyncio.run(main())