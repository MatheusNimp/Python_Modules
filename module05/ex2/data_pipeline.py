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


class ExportPlugin(typing.Protocol):
    """Duck-typed export contract."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Consume exported values from processors."""


class CSVExportPlugin:
    """Export values as a single CSV line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [self._escape_csv(value) for _, value in data]
        print("CSV Output:")
        print(",".join(values))

    @staticmethod
    def _escape_csv(value: str) -> str:
        escaped = value.replace('"', '""')
        if any(char in value for char in [',', '"', '\n']):
            return f'"{escaped}"'
        return escaped


class JSONExportPlugin:
    """Export values as a JSON object string."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for rank, value in data:
            escaped = self._escape_json(value)
            items.append(f'"item_{rank}": "{escaped}"')
        print("JSON Output:")
        print("{" + ", ".join(items) + "}")

    @staticmethod
    def _escape_json(value: str) -> str:
        return (
            value.replace('\\', '\\\\')
            .replace('"', '\\"')
            .replace('\n', '\\n')
        )


class DataStream:
    """Route a heterogeneous stream and export processed output."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(element):
                    try:
                        processor.ingest(element)
                        handled = True
                        break
                    except ValueError as exc:
                        print(f"DataStream error - {exc}: {element}")
                        handled = True
                        break
            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            print(
                f"{processor.name}: total {processor.total_processed} "
                f"items processed, remaining {processor.remaining} "
                "on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            exported: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    exported.append(processor.output())
                except IndexError:
                    break
            if exported:
                plugin.process_output(exported)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    print("\nRegistering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(logs)

    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
