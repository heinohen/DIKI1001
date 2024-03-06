
import spacy

nlp = spacy.load("en_core_web_sm") #small english
doc = nlp("Berlin looks like a nice city")

# Get all tokens and part-of-speech tags

for token in doc:
    if token.pos_  == "PROPN":
        ahead = token.i + 1
        if ahead < len(doc) and doc[ahead].pos_ == "VERB":
            result = token.text
            print("Found proper noun before a verb:", result)
            