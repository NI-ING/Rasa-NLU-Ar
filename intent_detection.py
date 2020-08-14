
# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config  


def intent_detection (MODEL_DIRECTORY,txt):


	from rasa_nlu.model import Metadata, Interpreter

	interpreter = Interpreter.load(MODEL_DIRECTORY)

	return interpreter.parse(txt)







