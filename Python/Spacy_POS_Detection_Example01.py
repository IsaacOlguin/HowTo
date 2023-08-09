import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
ENTITIES = ["NOUN", "PRON", "PROPN"]

for token in doc:
    print(f'{token.text}\t{token.lemma_}\t{token.pos_}\t{token.tag_}\t{token.dep_}\t{token.shape_}\t{token.is_alpha}\t{token.is_stop}')
