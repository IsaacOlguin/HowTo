#===================================================================================

import nltk
import pandas as pd
from nltk.tokenize import RegexpTokenizer

#===================================================================================

try:
    nltk.download('punkt')
except:
    print("It was not possible to download 'punkt'")
try:
    nltk.download('averaged_perceptron_tagger')
except:
    print("It was not possible to download 'averaged_perceptron_tagger")

#===================================================================================

def retrieve_one_row_column_from_dataframe(dataframe, index_row, name_column=None):
    for index, row in dataframe[index_row:index_row+1].iterrows():
        if name_column == None:
            return row
        else:
            return row[name_column]

def print_text_of_row_column_from_dataframe(dataframe, index_row, name_column=None):
    print(retrieve_one_row_column_from_dataframe(dataframe=dataframe, index_row=index_row, name_column=name_column))

def retrieve_string_of_tags_from_nltk_tuple(list_of_tuples_word_tag=list(), debug=False):
    if not type(list_of_tuples_word_tag) == list:
        print(f"The received parameter is not from the desired type 'list'. Got {type(list_of_tuples_word_tag)}")
        return None
    list_tags = list()
    for (word, tag) in list_of_tuples_word_tag:
        list_tags.append(tag)
        if debug:
            print(f"Word [{word}] --- Tag [{tag}]")

    return " ".join(list_tags)

#===================================================================================

example_dict = [
    {
        "text" : "This is an example of a text that I need to use for extracting key words"
    }
]

#===================================================================================

dataframe = pd.DataFrame.from_records(example_dict)
print(dataframe.head())

dataframe["tokenized"] = dataframe["text"].str.lower().apply(nltk.word_tokenize)
print("TOKENIZED => ", end="")
print_text_of_row_column_from_dataframe(dataframe=dataframe, index_row=0, name_column="tokenized")

dataframe["tagged"] = dataframe["tokenized"].apply(nltk.pos_tag)
print("TAGGED => ", end="")
print_text_of_row_column_from_dataframe(dataframe=dataframe, index_row=0, name_column="tagged")

list_of_tuples_word_tag = retrieve_one_row_column_from_dataframe(dataframe=dataframe, index_row=0, name_column="tagged")
print(list_of_tuples_word_tag)

list_tags_as_str = retrieve_string_of_tags_from_nltk_tuple(list_of_tuples_word_tag)
print(f"list_tags_as_str <<{list_tags_as_str}>>")

tokenizer = RegexpTokenizer(r'(NN.|JJ) (NN.*)')
print(tokenizer.tokenize(list_tags_as_str))