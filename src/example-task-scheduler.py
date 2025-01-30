from datetime import datetime, timedelta, timezone
from lib.task import CarbonAwareTask
from lib.scheduler import determine_optimal_execution_time, determine_now_execution
import openapi_client
from openapi_client.rest import ApiException



task = CarbonAwareTask(
    execution_path="path/path/hola",
    execution_region="belgium",
    estimated_duration=timedelta(hours=1),
    max_wait_time=timedelta(hours=2),
    ingestion_time=datetime(2025, 1, 31, 0, 0)
)

optimal_time = determine_optimal_execution_time(task)
print(f"The optimal time to execute the task is: {optimal_time}")



tasks = [
    CarbonAwareTask(
        execution_path="path/to/task1",
        execution_region="belgium",
        estimated_duration=timedelta(hours=1),
        max_wait_time=timedelta(hours=2),
        ingestion_time=datetime(2025, 1, 31, 0, 0)
    ),
    CarbonAwareTask(
        execution_path="path/to/task2",
        execution_region="belgium",
        estimated_duration=timedelta(hours=1),
        max_wait_time=timedelta(hours=2),
        ingestion_time=datetime(2025, 1, 31, 1, 0)
    ),
    CarbonAwareTask(
        execution_path="path/to/task3",
        execution_region="belgium",
        estimated_duration=timedelta(hours=1),
        max_wait_time=timedelta(hours=2),
        ingestion_time=datetime(2025, 1, 31, 2, 0)
    )
]

tasks_to_execute_now = determine_now_execution(tasks)
print(f"Tasks that can be executed now: {tasks_to_execute_now}")