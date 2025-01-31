from datetime import datetime, timedelta, timezone
from src.lib.task import CarbonAwareTask
import openapi_client
from openapi_client.rest import ApiException


HOST = "https://carbon-aware-sdk-api-808362706826.europe-west1.run.app"
CONFIGURATION = openapi_client.Configuration(
    host = HOST,
)

def determine_optimal_execution_time(task: CarbonAwareTask) -> datetime:
    """Determines the optimal time to execute a CarbonAwareTask using the carbon aware sdk."""

    with openapi_client.ApiClient(CONFIGURATION) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.CarbonAwareApi(api_client)

        try:
            api_response = api_instance.get_current_forecast_data(
                location=['belgium'],
                data_start_at=task.ingestion_time,
                data_end_at=task.ingestion_time + task.max_wait_time,
                window_size = int(task.estimated_duration.total_seconds() / 60),
            )

        except ApiException as e:
            raise Exception("Exception when calling CarbonAwareApi: %s\n" % e)

        forecast_data = api_response[0]
        optimal_time = forecast_data.optimal_data_points[0].timestamp

    if optimal_time is None:
        raise ValueError("No optimal execution time found.")


    return optimal_time



def determine_now_execution(tasks: list[CarbonAwareTask]) -> list[CarbonAwareTask]:
    """Determines which CarbonAwareTasks should be executed now based on the optimal execution time."""

    now = datetime.now(timezone.utc)
    executable_tasks = []

    for task in tasks:
        try:
            # Try to get the optimal execution time for the task
            optimal_time = determine_optimal_execution_time(task)

            # Check if the optimal execution time is within the current hour
            if now <= optimal_time < (now + timedelta(hours=1)):
                executable_tasks.append(task)

        except ValueError as e:
            # Handle the case where no optimal time is found
            print(f"Warning: No optimal execution time found for task {task.execution_path}. Skipping task.")
            # Optionally, log the error or take other actions if needed


    return executable_tasks



