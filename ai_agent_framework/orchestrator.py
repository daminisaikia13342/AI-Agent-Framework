import time
import logging
from executors import EXECUTORS
from state_store import StateStore
from observability import trace, Metrics

class Orchestrator:
    def __init__(self):
        self.state = StateStore()
        self.metrics = Metrics()

    def run(self, workflow: dict, initial_input):
        logging.info(f"Workflow started: {workflow['flow_id']}")
        current_input = initial_input

        for task in workflow["tasks"]:
            name = task["name"]
            executor_type = task["type"]
            retries = task.get("retries", 1)
            timeout = task.get("timeout", 30)

            executor = EXECUTORS[executor_type]
            success = False

            for attempt in range(1, retries + 1):
                try:
                    with trace(name):
                        start = time.time()
                        output = executor.execute(current_input, self.state.snapshot())
                        elapsed = time.time() - start

                        if elapsed > timeout:
                            raise TimeoutError("Task exceeded timeout")

                        self.state.write(name, output)
                        current_input = output
                        self.metrics.record(name, elapsed)
                        success = True
                        break

                except Exception as e:
                    logging.error(f"{name} failed attempt {attempt}: {e}")

            if not success:
                raise RuntimeError(f"Workflow aborted at task: {name}")

        logging.info("Workflow completed successfully")
        return {
            "state": self.state.snapshot(),
            "metrics": self.metrics.export()
        }
