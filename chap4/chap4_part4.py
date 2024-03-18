import json
import spacy

from spacy.matcher import Matcher
from spacy.tokens import Span, DocBin


with open('assets/iphone.json', "r", encoding='utf8') as file:
    TEXTS = json.loads(file.read())

nlp = spacy.blank('en')
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]

# Add patterns to the matcher and create docs with matched entities

matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)

doc_bin = DocBin(docs = docs)
doc_bin.to_disk('./data/train.spacy')