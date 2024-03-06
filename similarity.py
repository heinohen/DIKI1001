import spacy
nlp = spacy.load("en_core_web_md")
# Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2)) # 0.869833325851152
# compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2)) # 0.685019850730896
#compare a document with a token
doc = nlp("I like pizza")
token = nlp("soap")[0]
print(doc.similarity(token)) # 0.18213694934365615
# Compare a span with a document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")
print(span.similarity(doc)) # 0.47190033157126826

like = nlp("I like cats")
hate = nlp("I hate cats")

print(like.similarity(hate))

