from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict, Union


Stats = Dict[str, Union[str, int, float]]


class DataStream(ABC):
    """Abstract base class for polymorphic stream handlers."""

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.batches_processed: int = 0
        self.items_processed: int = 0
        self.failures: int = 0
        self.last_error: Optional[str] = None

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        raise NotImplementedError

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """
        Default filter:
        - If criteria is None: return everything.
        - If criteria is a string: keep only string items containing it.
        """
        if criteria is None:
            return data_batch
        return [x for x in data_batch
                if isinstance(x, str) and criteria.lower() in x.lower()]

    def get_stats(self) -> Stats:
        """Return basic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "batches_processed": self.batches_processed,
            "items_processed": self.items_processed,
            "failures": self.failures,
        }

    def _fail(self, err: Exception) -> None:
        self.failures += 1
        self.last_error = str(err)


class SensorStream(DataStream):
    """Processes environmental sensor readings like 'temp:22.5'."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            strings: List[str] = [x for x in data_batch if isinstance(x, str)]
            temps: List[float] = [
                float(x.split(":", 1)[1].strip())
                for x in strings
                if x.lower().strip().startswith("temp:")
            ]

            self.batches_processed += 1
            self.items_processed += len(strings)

            if not temps:
                return (f"Sensor analysis: {len(strings)} readings processed, "
                        "no temp readings")

            avg_temp: float = sum(temps) / len(temps)
            return (f"Sensor analysis: {len(strings)} readings processed, "
                    f"avg temp: {avg_temp:.1f}C")
        except (ValueError, TypeError, IndexError) as e:
            self._fail(e)
            return f"Sensor processing failed: {e}"


class TransactionStream(DataStream):
    """Processes transactions like 'buy:100' and 'sell:150'."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            ops: List[str] = [x for x in data_batch if isinstance(x, str)]

            parsed: List[tuple[str, int]] = []
            for x in ops:
                if ":" not in x:
                    continue
                action, value = x.split(":", 1)
                parsed.append((action.strip().lower(), int(value.strip())))

            net: int = 0
            count: int = 0
            for action, value in parsed:
                if action == "buy":
                    net += value
                    count += 1
                elif action == "sell":
                    net -= value
                    count += 1

            self.batches_processed += 1
            self.items_processed += len(ops)

            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {net:+d} units")
        except (ValueError, TypeError) as e:
            self._fail(e)
            return f"Transaction processing failed: {e}"


class EventStream(DataStream):
    """Processes system events like 'login', 'error', 'logout'."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events: List[str] = [
                x.strip().lower() for x in data_batch if isinstance(x, str)
            ]
            errors: int = sum(1 for e in events if e == "error")

            self.batches_processed += 1
            self.items_processed += len(events)

            return (f"Event analysis: {len(events)} events, "
                    f"{errors} error detected")
        except (TypeError, ValueError) as e:
            self._fail(e)
            return f"Event processing failed: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """If criteria == 'error', keep only error events;
        otherwise use default."""
        if criteria is not None and criteria.strip().lower() == "error":
            return [x for x in data_batch
                    if isinstance(x, str) and x.strip().lower() == "error"]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    """Handles multiple stream types polymorphically (subtype polymorphism)."""

    def process(self, stream: DataStream, data_batch: List[Any]) -> str:
        """Process one batch through a stream, using the common interface."""
        return stream.process_batch(data_batch)

    def process_all(
            self, jobs: List[tuple[DataStream, List[Any]]]) -> List[str]:
        """Process multiple (stream, batch) pairs."""
        return [self.process(stream, batch) for stream, batch in jobs]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()

    jobs: List[tuple[DataStream, List[Any]]] = [
        (sensor, ["temp:31.0", "temp:25.0"]),
        (trans, ["buy:200", "sell:50", "buy:10", "sell:20"]),
        (event, ["login", "error", "error"]),
    ]

    results = processor.process_all(jobs)
    print("Batch 1 Results:")
    print(f"- Sensor data: {results[0]}")
    print(f"- Transaction data: {results[1]}")
    print(f"- Event data: {results[2]}")

    print("Stream filtering active: High-priority data only")
    filtered_sensor = sensor.filter_data(["temp:31.0", "humidity:10"], "temp")
    filtered_trans = trans.filter_data(["buy:200", "sell:50", "buy:10"], "buy")
    print(f"Filtered results: {len(filtered_sensor)} sensor alerts, "
          f"{len(filtered_trans)} large transaction(s)")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
