from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter

def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    trainer.persist(model_dir,fixed_model_name='Assistant')

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/Assistant')
    print(interpreter.parse(u'hello'))

if __name__=="__main__":
    train_nlu('./data/data.json', 'nlu_config.yml', './models/nlu')
    #run_nlu()
