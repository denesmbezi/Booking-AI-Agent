from llama-index.core.tools import FunctionTool
from pydantic import BaseModel, Field



def create_booking(booking: Booking) -> str:
    """
    Create a new booking with the provided details.

    Args:
        booking (Booking): The booking details.

    Returns:
        str: A confirmation message with the booking ID.
    """
    return f"Booking created successfully with ID: {booking.booking_id}"

