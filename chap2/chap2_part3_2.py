import spacy

#activate blank model
nlp = spacy.blank("en")

#import the Doc and Span class
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True,False]

# Create a Doc from the words and spaces

doc = Doc(nlp.vocab, words, spaces)

print(doc.text) # --> I like David Bowie

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"

span = Span(doc, 2, len(doc), label = "PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities

doc.ents = [span]

# print entities' text and labels

print([(ent.text, ent.label_) for ent in doc.ents])