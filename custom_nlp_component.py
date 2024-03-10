import spacy
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")

#Define custom component
@Language.component("custom_component") #decorator

def custom_component_function(doc):
    #do something to the doc here
    print(f'Doc length: {len(doc)}')
    #return the object back to pipeline
    return doc

# add as first in pipeline
nlp.add_pipe("custom_component", first=True)


# Location in the pipeline

# "last" | If true, add as last | ex. nlp.add_pipe("component", last=True)
# "first" | If true, add as first | ex. nlp.add_pipe("component", first=True)
# "before" | Add before component | ex. nlp.add_pipe("component", before="ner")
# "after" | Add after component | ex. nlp.add_pipie("component", after="tagger")
print(f'Pipeline: {nlp.pipe_names}')
# Pipeline: ['custom_component', 'tok2vec', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']

# Let's process a text!
doc = nlp("Hello World!")