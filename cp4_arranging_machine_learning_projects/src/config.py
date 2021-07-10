import os


# get current dir path
dir_path = os.path.dirname(os.path.realpath(__file__))

# get the parent path
parent_path = dir_path.split("/src")[0]

TRAINING_FILE = f"{parent_path}/input/mnist_train_folds.csv"

MODEL_OUTPUT = f"{parent_path}/models"