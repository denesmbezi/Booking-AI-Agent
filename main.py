from llama-index.core.tools import FunctionTool
from pydantic import BaseModel, Field



class Booking(BaseModel):
    booking_id: str = Field(..., description="The unique identifier for the booking")
    name: str = Field(..., description="The name of the customer who made the booking")
    email: str = Field(..., description="The email address of the customer")
    phone: str = Field(..., description="The phone number of the customer")


def create_booking(booking: Booking) -> str:
    """
    Create a new booking with the provided details.

    Args:
        booking (Booking): The booking details.

    Returns:
        str: A confirmation message with the booking ID.
    """
    return f"Booking created successfully with ID: {booking.booking_id}"

