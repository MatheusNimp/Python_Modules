import abc
import typing


NumericInput = int | float | list[int | float]
TextInput = str | list[str]
LogItem = dict[str, str]
LogInput = LogItem | list[LogItem]


class DataProcessor(abc.ABC):
    """Common base class for all processors."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._stored: list[tuple[int, str]] = []
        self._next_rank = 0
        self._total_processed = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        """Return True when the input can be ingested."""

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        """Ingest the given data into the processor."""

    def output(self) -> tuple[int, str]:
        """Return and remove the oldest stored item."""
        if not self._stored:
            raise IndexError(f"{self._name} has no data to output")
        return self._stored.pop(0)

    @property
    def name(self) -> str:
        return self._name

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._stored)

    def _store_many(self, values: list[str]) -> None:
        for value in values:
            self._stored.append((self._next_rank, value))
            self._next_rank += 1
            self._total_processed += 1


class NumericProcessor(DataProcessor):
    """Processor dedicated to numeric values."""

    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: typing.Any) -> bool:
        if self._is_numeric_value(data):
            return True
        if isinstance(data, list):
            return all(self._is_numeric_value(value) for value in data)
        return False

    def ingest(self, data: NumericInput) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self._store_many([str(value) for value in data])
            return
        self._store_many([str(data)])

    @staticmethod
    def _is_numeric_value(value: typing.Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)


class TextProcessor(DataProcessor):
    """Processor dedicated to text values."""

    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(value, str) for value in data)
        return False

    def ingest(self, data: TextInput) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._store_many(data)
            return
        self._store_many([data])


class LogProcessor(DataProcessor):
    """Processor dedicated to log dictionaries."""

    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: typing.Any) -> bool:
        if self._is_log_item(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_item(value) for value in data)
        return False

    def ingest(self, data: LogInput) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            self._store_many([self._render_log_item(item) for item in data])
            return
        self._store_many([self._render_log_item(data)])

    @staticmethod
    def _is_log_item(value: typing.Any) -> bool:
        if not isinstance(value, dict):
            return False
        return all(
            isinstance(key, str) and isinstance(item, str)
            for key, item in value.items()
        )

    @staticmethod
    def _render_log_item(item: LogItem) -> str:
        if "log_level" in item and "log_message" in item:
            return f"{item['log_level']}: {item['log_message']}"
        parts = [f"{key}={value}" for key, value in item.items()]
        return ", ".join(parts)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    print("\nTesting Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {logs.validate('Hello')}")
    log_batch = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_batch}")
    logs.ingest(log_batch)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = logs.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
