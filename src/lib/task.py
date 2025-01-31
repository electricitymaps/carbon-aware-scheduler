from dataclasses import dataclass
from datetime import timedelta, datetime

@dataclass
class CarbonAwareTask:
    execution_path: str
    execution_region: str
    estimated_duration: timedelta
    max_wait_time: timedelta
    ingestion_time: datetime

    def __post_init__(self):
        if isinstance(self.estimated_duration, int):
            self.estimated_duration = timedelta(minutes=self.estimated_duration)
        if isinstance(self.max_wait_time, int):
            self.max_wait_time = timedelta(minutes=self.max_wait_time)

    def execute(self):
        """Executes the task."""
        print(f"Executing task {self.execution_path} in region {self.execution_region}.")
