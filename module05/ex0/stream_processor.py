from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False

        count = 0
        for x in data:
            if not isinstance(x, (int, float)):
                return False
            count += 1

        if count == 0:
            return False

        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            counter = 0
            total = 0

            for x in data:
                counter += 1
                total += x

            avg = total / counter

            return (f"Processed {counter} numeric values"
                    f", sum={total}, avg={avg}")

        except Exception as error:
            return f"NumericProcessor error: {error}"


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data == "":
            return False

        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            char_count = 0
            word_count = 0
            in_word = False

            for char in data:
                char_count += 1

                if char != " " and not in_word:
                    word_count += 1
                    in_word = True
                elif char == " ":
                    in_word = False

            return (f"Processed text: {char_count} "
                    f"characters, {word_count} words")

        except Exception as error:
            return f"TextProcessor error: {error}"


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data == "":
            return False

        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            level = ""
            message = ""
            sep = False
            in_message = False

            for char in data:
                if not sep:
                    if char == ":":
                        sep = True
                    else:
                        level += char
                else:
                    if not in_message:
                        if char != " ":
                            message += char
                            in_message = True
                    else:
                        message += char

            if level == "ERROR":
                return "[ALERT] ERROR level detected: " + message

            if level == "WARNING":
                return "[WARNING] WARNING level detected: " + message

            return "[INFO] INFO level detected: " + message

        except Exception as error:
            return f"LogProcessor error: {error}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    print("Processing data:", [1, 2, 3, 4, 5])
    result = numeric.process([1, 2, 3, 4, 5])
    print("Validation: Numeric data verified")
    print(numeric.format_output(result))

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    result = text.process("Hello Nexus World")
    print("Validation: Text data verified")
    print(text.format_output(result))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    result = log.process("ERROR: Connection timeout")
    print("Validation: Log entry verified")
    print(log.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    index = 0
    count = 1

    while index < 3:
        result = processors[index].process(data_samples[index])
        print(f"Result {count}: "
              f"{processors[index].format_output(result)}")
        index += 1
        count += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
