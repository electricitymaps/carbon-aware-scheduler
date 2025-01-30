from src.lib.task import CarbonAwareTask

def load_tasks_from_db() -> list[CarbonAwareTask]:
    """Loads CarbonAwareTasks from the database."""
    raise NotImplementedError()

def overwrite_tasks_in_db(tasks: list[CarbonAwareTask]):
    """Overwrites the CarbonAwareTasks in the database."""
    raise NotImplementedError()