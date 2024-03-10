import spacy

#load a larger pipeline with vectors
nlp = spacy.load("en_core_web_md")

#compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))

#compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))

#compare a document with a token
doc_task = nlp("I like pizza")
token_task = nlp("soap")[0]
print(doc_task.similarity(token_task))

#compare a span with a document
span = nlp("I like pizza and pasta")[2:5]
doc_task2 = nlp("McDonalds sells burgers")
print(span.similarity(doc_task2))



# Similarity depends on the application context
# Useful for many applications: recommendation systems, flagging duplicates etc.
# There is no objective definition of "similarity"
# Depends on the context and what application needs to do

like = nlp("I like cats")
hate = nlp("I hate cats")

print(like.similarity(hate))