from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
import sys
import logging

logging.basicConfig(level=logging.ERROR)

# llm = ChatOpenAI(model="google/gemini-2.0-pro-exp-02-05:free", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
# planner_llm = ChatOpenAI(model="google/gemini-2.0-pro-exp-02-05:free", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
llm = ChatOpenAI(model="openai/gpt-4o-mini", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
# planner_llm = ChatOpenAI(model="openai/gpt-4o-mini", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))
# llm = ChatOpenAI(model="gpt-4o-mini")

initial_actions = [
	{'open_tab': {'url': 'https://www.google.com'}},
	{'open_tab': {'url': 'https://en.wikipedia.org/wiki/Randomness'}},
	{'scroll_down': {'amount': 1000}},
]

async def main():
    # Use command line argument if provided, otherwise use default
    task = sys.argv[1] if len(sys.argv) > 1 else "What is the meaning of life?"
    
    agent = Agent(
        task=task,
        llm=llm,
        # initial_actions=initial_actions,
        # planner_llm=planner_llm,
        # planner_interval=4,
    )
    history = await agent.run(max_steps=15)
    print("Got this answer: ")
    print(history.final_result())

asyncio.run(main())