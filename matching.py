import spacy

nlp = spacy.load("en_core_web_md")

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# Patterns are lists of dicts describing the tokens
pattern1 = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", [pattern1])

#Operators can specify how often a token should be matched
pattern2 = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}] # + op == one or more times

doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
print(matches) # each match is a tulpe (ID, start, end)

#Adding statistical prediction
matcher2 = Matcher(nlp.vocab)
matcher2.add("DOG", [[{"LOWER": "golden"}, {"LOWER": "retriever"}]])

dogger = nlp("I have a Golden Retriever")

for match_id, start, end, in matcher2(dogger):
    span = dogger[start:end]
    print(f'Matched span: {span.text}')
    # Get the span's root token and root head token
    print(f'Root token: {span.root.text}')
    print(f'Root head token {span.root.head.text}')
    # Get the previous token and its POS tag
    print(f'Previous token: {dogger[start -1].text} {dogger[start - 1].pos_}')