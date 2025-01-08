from autogen import Agent
from Agents.workers.advisor_worker_agent import AdvisorAgent

class ControllerAgent(Agent):
    def __init__(self, name):
        super().__init__(name=name)

    def communicate_with_worker(self, term):
        print(f"ControllerAgent: Communicating with worker agent AdvisorAgent")
        worker = AdvisorAgent(name="AdvisorAgent")
        result = worker.process_data(term)
        return result

