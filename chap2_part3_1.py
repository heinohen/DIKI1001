import spacy

#activate blank model
nlp = spacy.blank("en")

#import the Doc class
from spacy.tokens import Doc

# Desired text: "Oh, really?!"

words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Create a Doc from the words and spaces

doc = Doc(nlp.vocab, words, spaces)

print(doc.text)


