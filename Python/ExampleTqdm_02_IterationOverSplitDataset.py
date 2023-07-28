"""
import src.general_utilities as gral_utilities
import src.datasets_utilities as datasets_utilities
import src.preprocessing_utilities as preprocessing_utilities
import src.textrank_utilities as textrank_utilities
import src.extraction_sentences as extraction_sentences
"""

from tqdm import tqdm
from time import sleep
import numpy as np

data_train = range(9787)
data_dev = range(2186)
data_test = range(3231)
size_chunks = 10
text = ""

for class_i, data_i in zip(["train", "dev", "test"], [data_train, data_dev, data_test]):
    print(class_i, len(data_i))
    rangos = [data_train[i:i + size_chunks] for i in range(0, len(data_train), size_chunks)] 
    for rango in tqdm(rangos):
        #print(rango, rango[0], rango[-1])
        sleep(0.01)
        text += str(rango[0]) + " - " + str(rango[-1]) + "\n"

    print("\n\n")