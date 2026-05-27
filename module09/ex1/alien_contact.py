from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Allowed alien contact types."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validated model for an alien contact report."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Validate business rules that depend on multiple fields."""
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type is ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include received messages"
            )
        return self


def display_contact(contact: AlienContact) -> None:
    """Display the important details of a validated contact report."""
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message: '{contact.message_received}'")


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation message clearly."""
    first_error = error.errors()[0]
    print(first_error["msg"].removeprefix("Value error, "))


def main() -> None:
    """Demonstrate successful and failed alien contact validation."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-02-20T23:45:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Valid contact report:")
    display_contact(contact)
    print("=" * 38)
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-03-01T03:15:00",
            location="Lunar Outpost",
            contact_type="telepathic",
            signal_strength=4.2,
            duration_minutes=12,
            witness_count=1,
        )
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
