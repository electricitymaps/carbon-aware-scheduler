from src.lib.pub_sub import read_new_carbon_aware_tasks
from src.lib.scheduler import determine_now_execution
from src.lib.tasks_db import load_tasks_from_db, overwrite_tasks_in_db

def run():
    tasks = read_new_carbon_aware_tasks()
    tasks += load_tasks_from_db()
    tasks_to_execute = determine_now_execution(tasks)
    for task in tasks_to_execute:
        task.execute()
    remaining_tasks =  set(tasks) - set(tasks_to_execute)
    overwrite_tasks_in_db(list(remaining_tasks))

if __name__ == "__main__":
    run()