import os
import site
import sys


def is_virtual_environment() -> bool:
    """Return True when Python is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix or hasattr(sys, "real_prefix")


def get_environment_name() -> str:
    """Return the active virtual environment name."""
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return os.path.basename(virtual_env)
    return os.path.basename(sys.prefix)


def get_package_paths() -> list[str]:
    """Return known site-packages paths for the current Python environment."""
    try:
        return site.getsitepackages()
    except AttributeError:
        return [site.getusersitepackages()]


def print_global_environment_message() -> None:
    """Display guidance for users running outside a virtual environment."""
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")


def print_virtual_environment_message() -> None:
    """Display information about the active virtual environment."""
    print("\nMATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {get_environment_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    for package_path in get_package_paths():
        print(package_path)


def main() -> None:
    """Inspect and display the current Python execution environment."""
    if is_virtual_environment():
        print_virtual_environment_message()
    else:
        print_global_environment_message()


if __name__ == "__main__":
    main()
