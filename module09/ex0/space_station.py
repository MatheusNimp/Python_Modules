from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validated data model for a monitored space station."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    """Display the important details of a validated space station."""
    status = "Operational" if station.is_operational else "Offline"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation message clearly."""
    first_error = error.errors()[0]
    print(first_error["msg"])


def main() -> None:
    """Demonstrate successful and failed space station validation."""
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-01-15T10:30:00",
    )

    print("Valid station created:")
    display_station(station)
    print("=" * 40)
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="BAD01",
            name="Invalid Station",
            crew_size=25,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance="2024-01-15T10:30:00",
        )
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
