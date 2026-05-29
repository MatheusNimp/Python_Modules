import importlib
import sys


def import_dependency(name: str) -> object | None:
    """Import a dependency safely and return None when it is unavailable."""
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def get_version(module: object) -> str:
    """Return a module version when the module exposes one."""
    version = getattr(module, "__version__", "unknown")
    return str(version)


def check_dependencies() -> dict[str, object]:
    """Check required packages and display helpful dependency status lines."""
    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    loaded_modules: dict[str, object] = {}

    print("Checking dependencies:")
    for package_name, description in dependencies.items():
        module = import_dependency(package_name)
        if module is None:
            print(f"[MISSING] {package_name} - install this package")
            continue
        loaded_modules[package_name] = module
        print(f"[OK] {package_name} ({get_version(module)}) - {description}")

    return loaded_modules


def print_installation_help() -> None:
    """Print installation instructions for missing dependencies."""
    print("\nMissing programs detected.")
    print("Install dependencies with pip:")
    print("pip install -r requirements.txt")
    print("Or install dependencies with Poetry:")
    print("poetry install")
    print("Then run this program again.")


def show_dependency_management_notes() -> None:
    """Explain the difference between pip and Poetry dependency workflows."""
    print("Dependency management comparison:")
    print("pip reads requirements.txt and installs packages directly.")
    print("Poetry reads pyproject.toml and manages a project environment.")
    print("Poetry also maintains a lock file for reproducible installs.")


def analyze_matrix_data(
    pandas_module: object,
    numpy_module: object,
    pyplot_module: object,
) -> None:
    """Generate Matrix data with numpy, analyze it with pandas, and plot it."""
    np = numpy_module
    pd = pandas_module
    plt = pyplot_module

    print("Analyzing Matrix data...")

    rng = np.random.default_rng(seed=42)
    data_points = 1000
    ticks = np.arange(data_points)
    signal = rng.normal(loc=50.0, scale=12.0, size=data_points)
    glitches = rng.poisson(lam=4.0, size=data_points)
    anomaly_score = np.abs(signal - np.mean(signal)) + glitches

    frame = pd.DataFrame(
        {
            "tick": ticks,
            "signal": signal,
            "glitches": glitches,
            "anomaly_score": anomaly_score,
        }
    )

    print(f"Processing {len(frame)} data points...")
    summary = frame[["signal", "glitches", "anomaly_score"]].describe()
    print(summary)

    print("Generating visualization...")
    figure = plt.figure(figsize=(10, 6))
    axis = figure.add_subplot(1, 1, 1)
    axis.plot(frame["tick"], frame["signal"], label="Matrix signal")
    axis.plot(frame["tick"], frame["anomaly_score"], label="Anomaly score")
    axis.set_title("Matrix Data Analysis")
    axis.set_xlabel("Simulation tick")
    axis.set_ylabel("Value")
    axis.legend()
    axis.grid(True)
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    plt.close(figure)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Run the Matrix package-management demonstration."""
    print("LOADING STATUS: Loading programs...")
    loaded_modules = check_dependencies()
    show_dependency_management_notes()

    required_packages = {"pandas", "numpy", "matplotlib"}
    if set(loaded_modules) != required_packages:
        print_installation_help()
        sys.exit(1)

    pyplot_module = import_dependency("matplotlib.pyplot")
    if pyplot_module is None:
        print("[MISSING] matplotlib.pyplot - visualization unavailable")
        sys.exit(1)

    analyze_matrix_data(
        loaded_modules["pandas"],
        loaded_modules["numpy"],
        pyplot_module,
    )


if __name__ == "__main__":
    main()
