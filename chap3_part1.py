import spacy

# load the en_core_web_sm pipeline
nlp = spacy.load("en_core_web_sm")

# print the names of the pipeline components
print(nlp.pipe_names)

# print the full pipeline
print(nlp.pipeline)

# Whenever you're unsure about the current pipeline, you can
# inspect it by printing nlp.pipe_names or nlp.pipeline.