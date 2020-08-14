from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config




# In[ ]:


# Setting Up our Training Configuration with Spacy as Backend
# trainer = Trainer(config.load("config_spacy.yml"))
# trainer.train(training_data)
# model_directory = trainer.persist('projects/default/')

from rasa_nlu.model import Metadata, Interpreter


# In[ ]:


# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load("models/default/model_20200704-141658")


# In[ ]:


# Predicting
print(interpreter.parse("أريد أن أجد فندق"))





# In[ ]:


# print(interpreter.parse(u"9addech 3andi des points fel cart fid"))
