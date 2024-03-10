import spacy

from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print(f'animal_patterns {animal_patterns}')
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# Define the custom component
@Language.component("animal_component")
def animal_component_function(doc):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Overwrite the ents
    doc.ents = spans
    return doc


nlp.add_pipe("animal_component", after="ner")
print(nlp.pipe_names)

doc = nlp("I have a cat and a Golden Retriever")
print([ent.text, ent.label_] for ent in doc.ents)