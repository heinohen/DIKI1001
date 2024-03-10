import spacy

nlp = spacy.load("en_core_web_md")


# PART 1
part1 = nlp("Two bananas in pyjamas")
# Get the vector for the token "bananas"
bananas_vector = part1[1].vector
print(f'bananas_vector {bananas_vector}')

# PART 2
part2 = nlp("TV and books")
token1, token2 = part2[0], part2[2]
#get similarity
similarity = token1.similarity(token2)
print(f'similarity of TV / books {similarity}')

#PART 3

part3 = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = part3[3:5]
span2 = part3[12:len(part3)-1]
print(span1, span2)
# Get the similarity of the spans
similarity2 = span1.similarity(span2)
print(similarity2)