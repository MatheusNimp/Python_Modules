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
        filtered = {}
        if criteria is None:
            return data_batch
        for data in data_batch:
            if isinstance(data, str) and criteria in data:
                filtered += data
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "Generic"}


class SensorStream(DataStream):

    def process_batch(self, data_batch):
        pass

    def filter_data(self, data_batch, criteria = None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self):
        return super().get_stats()


class TransactionStream(DataStream):

    def process_batch(self, data_batch):
        pass

    def filter_data(self, data_batch, criteria = None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self):
        return super().get_stats()


class EventStream(DataStream):

    def process_batch(self, data_batch):
        pass

    def filter_data(self, data_batch, criteria = None):
        return super().filter_data(data_batch, criteria)

    def get_stats(self):
        return super().get_stats()
