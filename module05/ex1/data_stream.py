from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [d for d in data_batch if isinstance(d, str) and criteria in d]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "Generic"}


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch, criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch, criteria: Optional[str] = None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):

    def process_batch(self, data_batch):
        pass

    def filter_data(self, data_batch, criteria: Optional[str] = None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()
