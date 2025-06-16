from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.tools import FunctionTool
from agent.models import Booking
import os
from agent.agent import create_booking
load_dotenv()
api_key = os.getenv("OPEN_AI")
# Initialize the LLM
llm = OpenAI(api_key=api_key, model="gpt-4o")
# Define the tool using the function
get_booking_state_tool = FunctionTool.from_defaults(fn=create_booking, return_direct=True)
# Create the agent with the LLM and the tool
agent = FunctionAgent(llm=llm, tools=[get_booking_state_tool], verbose=True, system_prompt="You are a helpful booking agent that creates bookings based on user input.")
# Run the agent with a sample booking


import asyncio

async def main():
    response = await agent.run("Create a booking for John Doe on 2023-10-01 with booking ID 12345.his email address: johndoe@gmail.com and phone number: 123-456-7890.")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
