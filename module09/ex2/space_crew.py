from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Allowed ranks for space crew members."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validated information for one crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated mission with a nested crew list."""

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
        """Apply mission safety rules from the subject."""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not self.has_command_leader():
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365 and not self.has_experienced_crew():
            raise ValueError(
                "Long missions need 50% experienced crew"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def has_command_leader(self) -> bool:
        """Return True when the crew has a commander or captain."""

        command_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        return any(member.rank in command_ranks for member in self.crew)

    def has_experienced_crew(self) -> bool:
        """Return True when at least half the crew has 5+ years."""

        experienced_count = sum(
            1 for member in self.crew if member.years_experience >= 5
        )
        return experienced_count * 2 >= len(self.crew)


def show_mission(mission: SpaceMission) -> None:
    """Print mission and nested crew details."""

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


def show_validation_error(error: ValidationError) -> None:
    """Print the first Pydantic error message."""

    first_error = error.errors()[0]
    context = first_error.get("ctx")
    if isinstance(context, dict) and "error" in context:
        print(context["error"])
    else:
        print(first_error["msg"])


def main() -> None:
    """Create valid and invalid missions to demonstrate validation."""

    print("Space Mission Crew Validation")
    print("=" * 41)

    crew = [
        CrewMember(
            member_id="CMDR001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=42,
            specialization="Mission Command",
            years_experience=18,
        ),
        CrewMember(
            member_id="NAV002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=9,
        ),
        CrewMember(
            member_id="ENG003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=31,
            specialization="Engineering",
            years_experience=7,
        ),
    ]
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-11-20T14:00:00",
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    show_mission(mission)
    print("=" * 41)

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Moon Supply Run",
            destination="Moon",
            launch_date="2024-09-05T08:00:00",
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="SCI004",
                    name="Dana Lee",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Science",
                    years_experience=4,
                )
            ],
            budget_millions=300.0,
        )
    except ValidationError as error:
        show_validation_error(error)


if __name__ == "__main__":
    main()
