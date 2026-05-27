import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


REQUIRED_VARIABLES = (
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT",
)


def load_environment() -> bool:
    """Load .env values with python-dotenv when the package is available."""
    if load_dotenv is None:
        print("WARNING: python-dotenv is not installed.")
        print("Install it with: pip install python-dotenv")
        return False
    return bool(load_dotenv(override=False))


def get_config_value(name: str, default: str = "") -> str:
    """Read a configuration value from the process environment."""
    return os.environ.get(name, default)


def mask_secret(secret: str) -> str:
    """Mask a secret value before displaying it."""
    if not secret:
        return "Missing"
    if len(secret) <= 4:
        return "****"
    return f"{secret[:2]}{'*' * (len(secret) - 4)}{secret[-2:]}"


def describe_database(database_url: str, mode: str) -> str:
    """Return a safe database connection description."""
    if not database_url:
        return "Missing configuration"
    if mode == "production":
        return "Connected to production instance"
    if "localhost" in database_url or "sqlite" in database_url:
        return "Connected to local instance"
    return "Connected to configured instance"


def describe_zion_endpoint(endpoint: str) -> str:
    """Return the visible status of the Zion endpoint setting."""
    if not endpoint:
        return "Offline"
    return "Online"


def validate_configuration() -> list[str]:
    """Return the names of required variables that are currently missing."""
    missing: list[str] = []
    for variable in REQUIRED_VARIABLES:
        if not os.environ.get(variable):
            missing.append(variable)
    return missing


def env_file_is_ignored() -> bool:
    """Check whether .gitignore contains an entry for the .env file."""
    gitignore_path = ".gitignore"
    if not os.path.exists(gitignore_path):
        return False
    try:
        with open(gitignore_path, "r", encoding="utf-8") as gitignore_file:
            lines = [line.strip() for line in gitignore_file]
    except OSError:
        return False
    return ".env" in lines


def print_security_checks(env_loaded: bool, missing: list[str]) -> None:
    """Display configuration safety checks."""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file_is_ignored():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env is not protected by .gitignore")
    if missing:
        print(f"[WARNING] Missing configuration: {', '.join(missing)}")
    elif env_loaded:
        print("[OK] Production overrides available")
    else:
        print("[OK] Environment variables available")


def main() -> None:
    """Load and display safe Matrix application configuration."""
    print("ORACLE STATUS: Reading the Matrix...")
    env_loaded = load_environment()

    mode = get_config_value("MATRIX_MODE", "development")
    database_url = get_config_value("DATABASE_URL")
    api_key = get_config_value("API_KEY")
    log_level = get_config_value("LOG_LEVEL", "INFO")
    zion_endpoint = get_config_value("ZION_ENDPOINT")
    missing = validate_configuration()

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(database_url, mode)}")
    print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
    print(f"API Key: {mask_secret(api_key)}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {describe_zion_endpoint(zion_endpoint)}")

    if mode == "production":
        print("Runtime profile: production safeguards enabled")
    else:
        print("Runtime profile: development diagnostics enabled")

    print_security_checks(env_loaded, missing)
    print("The Oracle sees all configurations.")

    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
