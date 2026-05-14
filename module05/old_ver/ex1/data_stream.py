from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


Stats = Dict[str, Union[str, int, float]]


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.batches_processed: int = 0
        self.items_processed: int = 0
        self.failures: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria.lower() in item.lower()
        ]

    def get_stats(self) -> Stats:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "batches_processed": self.batches_processed,
            "items_processed": self.items_processed,
            "failures": self.failures,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.batches_processed += 1
            self.items_processed += len(data_batch)

            temperatures: List[float] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    value = float(item.split(":", 1)[1])
                    temperatures.append(value)

            if len(temperatures) == 0:
                return f"Sensor analysis: {len(data_batch)} readings processed"

            avg_temp = sum(temperatures) / len(temperatures)
            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception:
            self.failures += 1
            return "Sensor processing failed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            result: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    value = float(item.split(":", 1)[1])
                    if value >= 30:
                        result.append(item)
            return result
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.batches_processed += 1
            self.items_processed += len(data_batch)

            count = 0
            net_flow = 0

            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, value = item.split(":", 1)
                    value_int = int(value)

                    if action == "buy":
                        net_flow += value_int
                        count += 1
                    elif action == "sell":
                        net_flow -= value_int
                        count += 1

            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {net_flow:+d} units"
            )
        except Exception:
            self.failures += 1
            return "Transaction processing failed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    _, value = item.split(":", 1)
                    if int(value) >= 100:
                        result.append(item)
            return result
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.batches_processed += 1
            self.items_processed += len(data_batch)

            error_count = 0
            for item in data_batch:
                if isinstance(item, str) and item == "error":
                    error_count += 1

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} error detected"
            )
        except Exception:
            self.failures += 1
            return "Event processing failed"


class StreamProcessor:
    def process_stream(self, stream: DataStream, data_batch: List[Any]) -> str:
        return stream.process_batch(data_batch)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))

    print("\nInitializing Transaction Stream...")
    print(
        f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(["buy:100", "sell:150", "buy:75"]))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()

    sensor_batch = ["temp:31.0", "temp:25.0"]
    transaction_batch = ["buy:200", "sell:50", "buy:10", "sell:20"]
    event_batch = ["login", "error", "error"]

    processor.process_stream(sensor, sensor_batch)
    processor.process_stream(transaction, transaction_batch)
    processor.process_stream(event, event_batch)

    print("Batch 1 Results:")
    print(f"- Sensor data: {len(sensor_batch)} readings processed")
    print("- Transaction data: 4 operations processed")
    print(f"- Event data: {len(event_batch)} events processed")

    print("\nStream filtering active: High-priority data only")
    filtered_sensor = sensor.filter_data(sensor_batch, "critical")
    filtered_transaction = transaction.filter_data(transaction_batch, "large")
    print(
        f"Filtered results: {len(filtered_sensor)} critical sensor alerts, "
        f"{len(filtered_transaction)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
