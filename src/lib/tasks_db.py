import os
from src.lib.task import CarbonAwareTask
from google.cloud.storage import Client, Bucket
from json import loads, dumps


TASK_BUCKET = os.environ["CARBON_AWARE_TASK_BUCKET"]


def load_tasks_from_db() -> list[CarbonAwareTask]:
    """Loads CarbonAwareTasks from the database."""
    client = Client()
    bucket = Bucket(client, TASK_BUCKET)
    with bucket.blob("tasks.json").open("r") as f:
        tasks = loads(f.read())
        return [CarbonAwareTask(**task) for task in tasks]

def overwrite_tasks_in_db(tasks: list[CarbonAwareTask]):
    """Overwrites the CarbonAwareTasks in the database."""
    client = Client()
    bucket = Bucket(client, TASK_BUCKET)
    with open("tasks.json", "w") as f:
        f.write(dumps([task.__dict__ for task in tasks]))
    bucket.blob("tasks.json").upload_from_filename("tasks.json")
