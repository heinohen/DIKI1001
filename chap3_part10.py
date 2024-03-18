import spacy
from spacy.tokens import Doc

nlp = spacy.blank("en")

# Define the getter
def get_has_number(doc):
    # Return if any of the tokens in the doc return True for token.like_num
    return any(token.like_num for token in doc)

# Register the Doc property extension "has_number" with the getter get_has_number

Doc.set_extension("has_number", getter=get_has_number)

# Process the dext and check the custom has_number attribute

doc = nlp("The museum closed for five years in 2012")
print(f'has_number: {doc._.has_number}')


# Works for both written or literal numbers 'five' '2012'abs
# Works also if .blank('fi') == kuusi or 2012