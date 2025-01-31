from dataclasses import dataclass
from datetime import timedelta, datetime

@dataclass
class CarbonAwareTask:
    execution_path: str
    execution_region: str
    estimated_duration: timedelta
    max_wait_time: timedelta
    ingestion_time: datetime

    def execute(self):
        """Executes the task."""
        print(f"Executing task {self.execution_path} in region {self.execution_region}.")