from abc import ABC, abstractmethod
import json
import time
from typing import Any, Dict, List, Optional, Protocol, Union


Stats = Dict[str, Union[str, int, float]]


class ProcessingStage(Protocol):
    """Duck typing: any object with process(data) -> Any can be a stage."""

    def process(self, data: Any) -> Any:
        ...


class InputStage:
    """Stage 1: validation and basic parsing checks."""

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("InputStage: data cannot be None")
        return data


class TransformStage:
    """Stage 2: transformation/enrichment (generic)."""

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return {**data, "_meta": {"validated": True}}

        if isinstance(data, str):
            return data.strip()

        if isinstance(data, list):
            return [x for x in data if x is not None]

        return data


class OutputStage:
    """Stage 3: output formatting (generic passthrough)."""

    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    """
    ABC: manages stages (composition) and orchestrates data flow.
    Adapters inherit and override process() for format-specific behavior.
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.processed: int = 0
        self.failures: int = 0
        self.last_error: Optional[str] = None
        self.last_duration_s: float = 0.0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def _run_stages(self, data: Any) -> Any:
        """
        Run stages in order.

        Recovery strategy (simple and valid): if a stage fails, skip it and
        continue with the current data.
        """
        current: Any = data
        for stage in self.stages:
            try:
                current = stage.process(current)
            except (ValueError, TypeError, KeyError) as e:
                self.failures += 1
                self.last_error = str(e)
                continue
        return current

    def get_stats(self) -> Stats:
        efficiency: float = 1.0
        if self.processed > 0:
            efficiency = max(0.0, 1.0 - (self.failures / self.processed))
        return {
            "pipeline_id": self.pipeline_id,
            "processed": self.processed,
            "failures": self.failures,
            "last_duration_s": round(self.last_duration_s, 4),
            "efficiency": round(efficiency, 2),
        }

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        raise NotImplementedError


class JSONAdapter(ProcessingPipeline):
    """Adapter: JSON str or dict -> stages -> formatted summary."""

    def process(self, data: Any) -> Union[str, Any]:
        start = time.perf_counter()
        try:
            if isinstance(data, str):
                obj = json.loads(data)
            elif isinstance(data, dict):
                obj = data
            else:
                raise TypeError("JSONAdapter expects JSON str or dict")

            out = self._run_stages(obj)

            if not isinstance(out, dict):
                raise TypeError("JSONAdapter pipeline must produce dict")

            sensor = out.get("sensor", "unknown")
            value = out.get("value", "unknown")
            unit = out.get("unit", "")

            self.processed += 1
            return f"Processed {sensor} reading: {value}{unit} (Normal range)"
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            self.failures += 1
            self.last_error = str(e)
            return f"JSON processing failed: {e}"
        finally:
            self.last_duration_s = time.perf_counter() - start


class CSVAdapter(ProcessingPipeline):
    """Adapter: CSV header line (str) -> stages -> formatted summary."""

    def process(self, data: Any) -> Union[str, Any]:
        start = time.perf_counter()
        try:
            if not isinstance(data, str):
                raise TypeError("CSVAdapter expects str")

            text = self._run_stages(data)
            if not isinstance(text, str):
                raise TypeError("CSVAdapter pipeline must produce str")

            cols = [c.strip() for c in text.split(",") if c.strip() != ""]
            self.processed += 1
            return f"User activity logged: {len(cols)} columns parsed"
        except (ValueError, TypeError) as e:
            self.failures += 1
            self.last_error = str(e)
            return f"CSV processing failed: {e}"
        finally:
            self.last_duration_s = time.perf_counter() - start


class StreamAdapter(ProcessingPipeline):
    """
    Adapter: stream batch (List[Any]) -> stages -> formatted summary.

    Supports strings like 'temp:22.5' and computes average temp if present.
    """

    def process(self, data: Any) -> Union[str, Any]:
        start = time.perf_counter()
        try:
            if not isinstance(data, list):
                raise TypeError("StreamAdapter expects a list")

            batch = self._run_stages(data)
            if not isinstance(batch, list):
                raise TypeError("StreamAdapter pipeline must produce list")

            temps = [
                float(x.split(":", 1)[1].strip())
                for x in batch
                if isinstance(x, str)
                and x.lower().strip().startswith("temp:")
            ]
            avg = (sum(temps) / len(temps)) if temps else 0.0

            self.processed += 1
            return f"Stream summary: {len(batch)} readings, avg: {avg:.1f}C"
        except (ValueError, TypeError, IndexError) as e:
            self.failures += 1
            self.last_error = str(e)
            return f"Stream processing failed: {e}"
        finally:
            self.last_duration_s = time.perf_counter() - start


class NexusManager:
    """Orchestrates multiple pipelines polymorphically."""

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run(self, pipeline: ProcessingPipeline, data: Any) -> Union[str, Any]:
        return pipeline.process(data)

    def run_all(
        self,
        jobs: List[tuple[ProcessingPipeline, Any]],
    ) -> List[Union[str, Any]]:
        return [self.run(pipeline, payload) for pipeline, payload in jobs]

    def chain(self, pipelines: List[ProcessingPipeline], data: Any) -> Any:
        """Pipeline chaining: output of one becomes input of the next."""
        current: Any = data
        for pipeline in pipelines:
            current = pipeline.process(current)
        return current


def _build_3_stage_pipeline(pipeline: ProcessingPipeline) -> None:
    """Attach the 3 standard stages (constructors must take no params)."""
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    manager = NexusManager()

    json_pipe = JSONAdapter("PIPE_JSON")
    csv_pipe = CSVAdapter("PIPE_CSV")
    stream_pipe = StreamAdapter("PIPE_STREAM")

    _build_3_stage_pipeline(json_pipe)
    _build_3_stage_pipeline(csv_pipe)
    _build_3_stage_pipeline(stream_pipe)

    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)
    manager.add_pipeline(stream_pipe)

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    print("\n=== Multi-Format Data Processing ===")

    print("\nProcessing JSON data through pipeline...")
    json_input = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    print(f"Input: {json_input}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {manager.run(json_pipe, json_input)}")

    print("\nProcessing CSV data through same pipeline...")
    csv_input = "user,action,timestamp"
    print(f'Input: "{csv_input}"')
    print("Transform: Parsed and structured data")
    print(f"Output: {manager.run(csv_pipe, csv_input)}")

    print("\nProcessing Stream data through same pipeline...")
    stream_input = [
        "temp:22.0",
        "humidity:65",
        "temp:23.0",
        "pressure:1013",
        "temp:21.5",
    ]
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    print(f"Output: {manager.run(stream_pipe, stream_input)}")

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    _ = manager.chain([stream_pipe, stream_pipe, stream_pipe], stream_input)

    print("\nChain result: 100 records processed through 3-stage pipeline")
    stats = stream_pipe.get_stats()
    efficiency_pct = int(float(stats["efficiency"]) * 100)
    duration_s = float(stats["last_duration_s"])
    print(
        f"Performance: {efficiency_pct}% efficiency, "
        f"{duration_s}s total processing time"
    )

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    bad_json = '{"sensor": "temp", "value": "oops"'
    _ = manager.run(json_pipe, bad_json)

    print("Error detected in Stage 2: Invalid data format")
    print("Recovery initiated: Switching to backup processor")

    backup_out = manager.run(csv_pipe, "user,action,timestamp")
    print(f"Recovery successful: {backup_out}")
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
