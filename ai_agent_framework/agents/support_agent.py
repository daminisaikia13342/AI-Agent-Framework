import json
from orchestrator import Orchestrator

def run(input_data):
    with open("workflows/support_agent.json") as f:
        workflow = json.load(f)

    return Orchestrator().run(workflow, input_data)
