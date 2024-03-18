#Setting custom attributes

    # Add custom metadata to documents, tokens and spans
    # Accessible via the ._ property

# doc._.title = "My document"
# token._.is_color = True
# span._.has_color = False

# #  Registered on the global Doc, Token or Span using the set_extension method

# # Import global classes
# from spacy.tokens import Doc, Token, Span

# Set extensions on the Doc, Token and Span
# Doc.set_extension("title", default=None)
# Token.set_extension("is_color", default=False)
# Span.set_extension("has_color", default=False)

# from spacy.tokens import Token

# # Set extension on the Token with default value
# Token.set_extension("is_color", default=False)

# doc = nlp("The sky is blue.")

# # Overwrite extension attribute value
# doc[3]._.is_color = True

# from spacy.tokens import Token

# define getter

# def get_is_color(token):
    # colors = ["red", "yellow", "blue"]

# Set extension on the Token with getter

# Token.set_extension("is_color", getter = get_is_color)

# doc = nlp("The sky is blue")
# print(doc[3]._.is_color, "-", doc[3].text)


# from spacy.tokens import Span

# # Define getter function
# def get_has_color(span):
#     colors = ["red", "yellow", "blue"]
#     return any(token.text in colors for token in span)

# # Set extension on the Span with getter
# Span.set_extension("has_color", getter=get_has_color)

# doc = nlp("The sky is blue.")
# print(doc[1:4]._.has_color, "-", doc[1:4].text)
# print(doc[0:2]._.has_color, "-", doc[0:2].text)

# from spacy.tokens import Doc

# # Define method with arguments
# def has_token(doc, token_text):
#     in_doc = token_text in [token.text for token in doc]
#     return in_doc

# # Set extension on the Doc with method
# Doc.set_extension("has_token", method=has_token)

# doc = nlp("The sky is blue.")
# print(doc._.has_token("blue"), "- blue")
# print(doc._.has_token("cloud"), "- cloud")