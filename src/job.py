from src.lib.pub_sub import read_new_carbon_aware_tasks
from src.lib.executer import execute_task
from src.lib.scheduler import determine_optimal_execution_time
from src.lib.tasks_db import load_tasks_from_db, overwrite_tasks_in_db

def run():
    project_id = "my_project_id"
    subscription_id = "my_subscription_id"
    tasks = read_new_carbon_aware_tasks(project_id, subscription_id)
    tasks += load_tasks_from_db()
    for task in tasks:
        optimal_execution_time = determine_optimal_execution_time(task)
        if optimal_execution_time <= task.deadline:
            execute_task(task)
        else:
            print(f"Task {task} is not executed because it is not optimal to execute it now.")
    overwrite_tasks_in_db(tasks)

if __name__ == "__main__":
    run()