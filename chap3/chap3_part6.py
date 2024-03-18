import spacy
from spacy.language import Language

#Define a custom component
@Language.component("length_component")
def length_component_function(doc):
    print(f'This document is {len(doc)} tokens long.')
    return doc


nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("length_component", first=True)


doc = nlp("This is a sentence.")