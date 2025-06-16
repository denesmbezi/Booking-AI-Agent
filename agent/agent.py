from llama_index.core.tools import FunctionTool
from typing import List
from agent.models import Booking

def create_booking(booking: Booking) -> str:
    """
    Create a new booking with the provided details.

    Args:
        booking (Booking): The booking details.

    Returns:
        str: A confirmation message with the booking ID.
    """
    return f"Booking created successfully with ID:"



get_booking_state_tool = FunctionTool.from_defaults(fn=create_booking, return_direct=True)



