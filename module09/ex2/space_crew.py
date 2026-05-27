from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Allowed ranks for crew members."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validated model for one crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated model for a space mission and its crew."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Validate safety rules that depend on the mission crew."""
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not self._has_commanding_officer():
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365 and not self._has_enough_experience():
            raise ValueError(
                "Long missions need 50% experienced crew (5+ years)"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def _has_commanding_officer(self) -> bool:
        """Return True when the crew has a commander or captain."""
        command_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        return any(member.rank in command_ranks for member in self.crew)

    def _has_enough_experience(self) -> bool:
        """Return True when at least half the crew has 5+ years."""
        experienced_count = sum(
            1 for member in self.crew if member.years_experience >= 5
        )
        return experienced_count * 2 >= len(self.crew)


def display_mission(mission: SpaceMission) -> None:
    """Display the important details of a validated mission."""
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def print_first_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic validation message clearly."""
    first_error = error.errors()[0]
    print(first_error["msg"].removeprefix("Value error, "))


def build_valid_mission() -> SpaceMission:
    """Create a valid demonstration mission."""
    return SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-09-15T08:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank="commander",
                age=45,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank="lieutenant",
                age=34,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank="officer",
                age=29,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
    )


def main() -> None:
    """Demonstrate successful and failed mission validation."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    mission = build_valid_mission()

    print("Valid mission created:")
    display_mission(mission)
    print("=" * 41)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Uncommanded Test Mission",
            destination="Europa",
            launch_date="2024-11-01T09:00:00",
            duration_days=30,
            budget_millions=300.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob Stone",
                    rank="officer",
                    age=31,
                    specialization="Science",
                    years_experience=4,
                )
            ],
        )
    except ValidationError as error:
        print_first_validation_error(error)


if __name__ == "__main__":
    main()
