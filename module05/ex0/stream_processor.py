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
        return "Output" + result


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

    def process(self, data):
        if not self.validate(data):
            return "Error in validation"

        counter = 0
        total = 0

        for x in data:
            counter += 1
            sum += x

        print(f"Processed {counter} numeric values, sum={sum}, avg={}")


class TextProcessor(DataProcessor):

    def validate(self, data):
        if not data:
            return False
        if not isinstance(data, (str)):
            return False

        return True


class LogProcessor(DataProcessor):

    def validate(self, data):
        if not data:
            return False
        if not isinstance(data, (str)):
            return False

        return True
