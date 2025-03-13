from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
import sys
import logging

logging.basicConfig(level=logging.ERROR)

llm = ChatOpenAI(model="openai/gpt-4o-mini", base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

initial_actions = [
	{'open_tab': {'url': 'https://www.picknsave.com'}},
    {"click_element":{"index":10}},
    {"click_element":{"index":11}},
    {"wait": {"seconds": 10}},
    {"input_text":{"index":2,"text":os.getenv("PICKNSAVE_EMAIL")}},
    {"input_text":{"index":3,"text":os.getenv("PICKNSAVE_PASSWORD")}},
    {"click_element":{"index":7}},
]

async def main():
    # Use command line argument if provided, otherwise use default
    task = sys.argv[1] if len(sys.argv) > 1 else "What is the meaning of life?"
    task += "\n\nIMPORTANT! NEVER spend money by checking out or donating or anything on behalf of the user. They may be signed in. You can add items to the cart or search, but never go through a check out process or otherwise spend any money. Refuse if they ask." 
    agent = Agent(
        task=task,
        llm=llm,
        #initial_actions=initial_actions,
        planner_llm=llm,
        planner_interval=4,
    )
    history = await agent.run(max_steps=100)
    print("Got this answer: ")
    print(history.final_result())

asyncio.run(main())
