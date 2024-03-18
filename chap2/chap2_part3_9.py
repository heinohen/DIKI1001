import json, spacy

#import the PhraseMatcher

from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

with open("assets/countries.json", encoding="utf8") as file:
    COUNTRIES = json.loads(file.read())

with open("assets/country_text.txt", encoding="utf8") as file:
    TEXT = file.read()

nlp = spacy.load("en_core_web_sm")
# Create pattern Doc obbjects and add them to the matcher
# This is the faster version of: [nlp(country) for country in COUNTRIES]
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY",patterns)

doc = nlp(TEXT)
doc.ents = []

for match_id, start, end in matcher(doc):
    # Create a span with the label "GPE" Geo Political Entity
    span = Span(doc, start, end, label="GPE")
    doc.ents = list(doc.ents) + [span]

    span_root_head = span.root.head
    print(f'{span_root_head.text} --> {span.text}')

    print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])




