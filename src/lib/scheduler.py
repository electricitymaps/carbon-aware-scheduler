from datetime import datetime, timedelta, timezone
from lib.task import CarbonAwareTask
import openapi_client
from openapi_client.rest import ApiException


def determine_optimal_execution_time(task: CarbonAwareTask) -> datetime:
    """Determines the optimal time to execute a CarbonAwareTask using the carbon aware sdk."""

    configuration = openapi_client.Configuration(
    host = "http://localhost:5073",
    )
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.CarbonAwareApi(api_client)

        try:
            api_response = api_instance.get_current_forecast_data(
                location=['belgium'],
            )
            # for e in api_response:
            #     print(e.to_str())
        except ApiException as e:
            print("Exception when calling CarbonAwareApi: %s\n" % e)
    # Find the optimal time based on emissions (lowest emissions value)
    optimal_time = None
    min_emissions = float('inf')

    forecast_data = api_response[0].forecast_data

    for data_point in forecast_data:

        task_ingestion_time = task.ingestion_time.replace(tzinfo=timezone.utc)
        task_end_time = (task.ingestion_time + task.max_wait_time).replace(tzinfo=timezone.utc)

        if task_ingestion_time <= data_point.timestamp <= task_end_time:
            if data_point.value < min_emissions:
                min_emissions = data_point.value
                optimal_time = data_point.timestamp

    if optimal_time is None:
        raise ValueError("No optimal execution time found.")

    return optimal_time



def determine_now_execution(tasks: list[CarbonAwareTask]) -> list[CarbonAwareTask]:
    """Determines which CarbonAwareTasks should be executed now based on the optimal execution time."""

    now = datetime.now(timezone.utc)
    executable_tasks = []

    for task in tasks:
        optimal_time = determine_optimal_execution_time(task)

        # Check if the optimal execution time is within the current hour
        if now <= optimal_time < (now + timedelta(hours=1)):
            executable_tasks.append(task)

    return executable_tasks



