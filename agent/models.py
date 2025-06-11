from pydantic import BaseModel, Field


class Booking(BaseModel):
    booking_id: str = Field(..., description="The unique identifier for the booking")
    name: str = Field(..., description="The name of the customer who made the booking")
    email: str = Field(..., description="The email address of the customer")
    phone: str = Field(..., description="The phone number of the customer")