import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_md")

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", [pattern])

doc = nlp("I have a Golden Retriever")

# Iterate over matches

for match_i, start, end in matcher(doc):
    # get matched span
    span = doc[start:end]
    print(f'Matched span: {span.text}')

