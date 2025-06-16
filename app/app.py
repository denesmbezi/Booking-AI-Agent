from agent.models import Booking


def create_booking(booking: Booking) -> str:
    """
    Create a booking based on the provided booking details.

    Args:
        booking (Booking): The booking details.

    Returns:
        str: A confirmation message with the booking details.
    """
    if not booking.name or not booking.date or not booking.booking_id:
        raise ValueError("Booking must have a name, date, and booking ID.")
    if not booking.email or not booking.phone:
        raise ValueError("Booking must have an email and phone number.")
    # Here you would typically save the booking to a database or perform some action.
    # For this example, we will just return a confirmation message.
    if not isinstance(booking, Booking):
        raise TypeError("Expected booking to be an instance of Booking class.")
    if not booking.date:
        raise ValueError("Booking date cannot be empty.")
    if not booking.booking_id:
        raise ValueError("Booking ID cannot be empty.")
    if not booking.email:
        raise ValueError("Booking email cannot be empty.")
    if not booking.phone:
        raise ValueError("Booking phone number cannot be empty.")
    if not booking.name:
        raise ValueError("Booking name cannot be empty.")   
    return f"Booking created for {booking.name} on {booking.date} with ID {booking.booking_id}. Email: {booking.email}, Phone: {booking.phone}."