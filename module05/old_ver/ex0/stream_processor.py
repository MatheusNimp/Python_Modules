from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.processor_name: str = self.__class__.__name__

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            total = sum(data)
            count = len(data)
            avg = total / count
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as error:
            return f"NumericProcessor error: {error}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and data != ""

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            char_count = len(data)
            word_count = len(data.split())
            return (f"Processed text: {char_count} "
                    f"characters, {word_count} words")
        except Exception as error:
            return f"TextProcessor error: {error}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()

            if level == "ERROR":
                return f"[ALERT] ERROR level detected: {message}"
            if level == "WARNING":
                return f"[WARNING] WARNING level detected: {message}"
            return f"[INFO] INFO level detected: {message}"
        except Exception as error:
            return f"LogProcessor error: {error}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    print("Processing data:", [1, 2, 3, 4, 5])
    print("Validation: Numeric data verified")
    print(numeric.format_output(numeric.process([1, 2, 3, 4, 5])))

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    print("Validation: Text data verified")
    print(text.format_output(text.process("Hello Nexus World")))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    print("Validation: Log entry verified")
    print(log.format_output(log.process("ERROR: Connection timeout")))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    samples: list[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    index = 0
    while index < len(processors):
        result = processors[index].process(samples[index])
        print(f"Result {index + 1}: {result}")
        index += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
