import os
import pandas as pd
import matplotlib.pyplot as plt
from rasa_nlu.model import Trainer
#from rasa_nlu.evaluate import run_evaluation
from rasa_nlu.test import run_evaluation

from rasa_nlu import config
from rasa_nlu.training_data import load_data
import random
import time

# retrieving the initial training data of minotaur as a pd
initial_data = pd.read_json("data/json_data.json")


"""
Function to sample the training and test examples from the list of examples
initial_data is a dataframe composed of the list of all examples we want to sample from
nb_of_examples is the number of examples we want for both training and testing
"""
def select_examples(initial_data, nb_of_examples):
   # if too many examples asked to take all the examples and divided them in 20% 80%
   if nb_of_examples > len(initial_data["rasa_nlu_data"]["common_examples"]):
           nb_of_examples = len(initial_data["rasa_nlu_data"]["common_examples"])
   # list of examples for training data
   training_examples_list = []
   # list of examples for test data
   test_examples_list = []
   # copy the examples dataframe to remove select directly the rows to keep for training and test
   training_df = initial_data.copy()
   test_df = initial_data.copy()
   # Dataframe of examples
   examples_df = pd.DataFrame.from_records(initial_data["rasa_nlu_data"]["common_examples"])
   # a series that contains for each intent the percentage of examples
   serie_distOfExamples = examples_df["intent"].value_counts()/len(examples_df)
   for intent in serie_distOfExamples.index.values:
       # n is the number of examples for intent to keep: for both training and testing
       n=int(serie_distOfExamples[intent]*nb_of_examples)
       # the list of indexes for "intent" in the dataframe
       l = examples_df[examples_df["intent"] == intent].index.values
       # select randomly n indexes in l
       examples_samp = random.sample(list(l),n)
       # 80% of those examples are kept for training
       training_examples_ids = random.sample(examples_samp,int(n*0.8))
       # the rest is for testing
       for ex_id in training_examples_ids:
           examples_samp.remove(ex_id)
       for index_train in training_examples_ids:
           training_examples_list.append(initial_data["rasa_nlu_data"]["common_examples"][index_train])
       for index_test in examples_samp:
           test_examples_list.append(initial_data["rasa_nlu_data"]["common_examples"][index_test])
   # we replace for both training and testing df the corresponding intent rows by the one we selected
   training_df["rasa_nlu_data"]["common_examples"] = training_examples_list
   test_df["rasa_nlu_data"]["common_examples"] = test_examples_list

   return training_df, test_df

#-------------------------------------------------------


# a function to reconstruct the JSON file for training and test examples from the output of the previous method
def construct_jsonExampleFile(training_df, test_df, initial_data):
    training_df.to_json('data/training_data.json')
    test_df.to_json('data/test_data.json')


#-----------------------------------------------------------------------------------------

def examplesDist_plot(log_pd):
    percent = pd.DataFrame.from_records(log_pd["rasa_nlu_data"]["common_examples"])["intent"].value_counts()
    percent.plot(kind='bar', figsize=(10,8))
    plt.ylabel("Number of examples per intent")
    plt.xlabel("Intents")
    plt.title("Number of examples per intent")
    # plt.grid()
    plt.show()

#---------------------------------------------------------------------------------------------


train,test=select_examples(initial_data,1000)
construct_jsonExampleFile(train,test,initial_data)
training_data = pd.read_json("data/training_data.json")
examplesDist_plot(training_data)



#----------------------------------------------------------------------------
def trainModel(pipeline,model_dir):
    path_to_data = "data/training_data.json"
    training_data = load_data(path_to_data)
    trainer = Trainer(config.load(pipeline))
    interpreter = trainer.train(training_data)
    path_to_model = "models/current/"+model_dir
    model_directory = trainer.persist(path_to_model)

    return model_directory


#-----------------------------------------------------------------------------


def evaluateModel(pathToData, model_dir):
    path_to_data = "data/test_data.json"

    # Create a directory if not exist.
    if not os.path.exists(model_dir +"/evaluation"):
        os.mkdir(model_dir +"/evaluation")
        print("Directory ", "evaluation", " Created ")

    # save the error file, Confusion matrix image, and histogram file
    errors_path = model_dir + "/evaluation/errors.json"
    confmat_path = model_dir + "/evaluation/confmat"
    intent_hist_path = model_dir + "/evaluation/hist"
    run_evaluation(path_to_data, model_dir, errors_filename=errors_path, confmat_filename=confmat_path,
                   intent_hist_filename=intent_hist_path)


#---------------------------------------------------------------------------------------


start = time.time()
model_dir = trainModel("config_spacy.yml","Tensorflow_embedings_modal")
end = time.time()
print("The training took ", (end-start)/60, " mins for execution")

# evaluation of the model
print(model_dir)
evaluateModel("548_training_examples",model_dir)








