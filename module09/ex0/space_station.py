from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validated report for a monitored space station."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def show_station(station: SpaceStation) -> None:
    """Print a station report in a clear review-friendly format."""

    status = "Operational" if station.is_operational else "Offline"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    print(f"Last maintenance: {station.last_maintenance.isoformat()}")
    if station.notes is not None:
        print(f"Notes: {station.notes}")


def show_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic error message."""

    first_error = error.errors()[0]
    context = first_error.get("ctx")
    if isinstance(context, dict) and "error" in context:
        print(context["error"])
    else:
        print(first_error["msg"])


def main() -> None:
    """Create valid and invalid stations to demonstrate validation."""

    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-03-10T09:30:00",
        notes="All core systems are stable.",
    )

    print("Valid station created:")
    show_station(station)
    print("=" * 40)

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Lunar Gateway",
            crew_size=25,
            power_level=75.0,
            oxygen_level=88.0,
            last_maintenance="2024-04-01T12:00:00",
        )
    except ValidationError as error:
        show_validation_error(error)


if __name__ == "__main__":
    main()
