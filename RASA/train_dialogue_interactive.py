import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

def run_trainer_online(interpreter, domain_file="assistant_domain.yml",training_data_file='data/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=5), KerasPolicy(max_history=5, epochs=100, batch_size=100)],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)

    data = agent.load_data(training_data_file)
    agent.train(data)
    interactive.run_interactive_learning(agent,training_data_file,skip_visualization=True)
    return agent

if __name__=="__main__":
    logging.basicConfig(level="INFO")

    nlu_intrepreter = RasaNLUInterpreter('./models/nlu/default/Assistant')
    run_trainer_online(nlu_intrepreter)
