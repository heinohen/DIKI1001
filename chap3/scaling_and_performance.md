# Processing large volume of text

Use `nlp.pipe` method

* Processes texts as a stream and yields 'Doc' objects
* Much faster than calling nlp on each text

## BAD

``` python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

## GOOD

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

## Passing in context

Setting `as_tuples=True` on nlp.pipe lets you pass in (text,context) tuples

* Yields (doc,context) tuples
* Useful for associating metadata with the `doc`

``` python
data = [
    ("This is a text", {"id":1, "page_number":15}),
    ("And another text"), {"id":2, "page_number":16}
    ]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
```

``` python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
```

### Using only the tokenizer

* Use `nlp.make_doc` to turn a text into a `Doc` object

BAD

```python
doc = nlp("hello world")
```

GOOD

```python
doc = nlp.make_doc("hello world!")
```

### Disabling pipeline components

* Use `nlp.select_pipes` to temporarily disable one or more pipes

```python
with nlp.select_pipes(disable=["tagger", "parser"]):
    doc = nlp(text)
    print(doc.ents)
```

* Restores them after the 'with' block, only runs the remaining components
