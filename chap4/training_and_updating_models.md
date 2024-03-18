# Why update model ?

1) Better results on your specific domain
2) Learn classification schemes specifically for your problem
3) Essential for text classification
4) Very useful for named entity recognition
5) Less critical for part-of-speech tagging and dependency parsing

## How training works

1) Initialize the model weights randomly
2) Predict a few examples with the current weights
3) Compare prediction with true labels
4) Calculate how to change weights to improve predictions
5) Update weights slightly
6) Go back to 2.

``` python
nlp.update
```

### Example

The entity recognizer tags words and phrases in context
Each token can only be part of one entity
Examples need to come with context

``` python
doc = nlp("iPhone X is coming")
doc.ents = [Span(doc,0,2,label="GADGET")]
```

Texts with no entities are also important

``` python
doc = nlp("I need a new phone! Any tips?")
doc.ents = []
```

Goal: Teach the model to generalize

## The training data

* Examples of what we want the model to predict in context.
* Update an existing model: a few hundred to a few thousand examples
* Train a new category: a few thousand to a million examples
  * spaCy's English models == 2 million words
* Usually created manyally by human annotators
* Can be saemi-automated - for example using spaCy's `matcher`

### Training vs evaluation data

* Training data: used to update the model
* Evaluation data:
  * data the model hasn't seen during training
  * used to calculate how accurate the model is
  * should be representative of the data the model will see at runtime

#### Generating a corpus

``` python
import spacy

nlp = spacy.blank('en')
# Create a Doc with entity spans
doc1 = nlp('iPhone X is coming')
doc1.ents = [Span(doc1,0,2, label="GADGET")]
doc2 = nlp('I need a new phone! Any tips?')

docs = [doc1,doc2]
# continues ... 
```

* Split the data into two portitions
  * Training data: used to update the model
  * Development data: used to evaluate the model

``` python
# ... continues
random.shuffle(docs)
train_docs = docs[:len(docs) // 2]
dev_docs = docs[len(docs) // 2:]
# continues ... 
```

* `DocBin`container to efficiently store and save `Doc` objects
* Can be saved to a binary file
* binary files are useful for training

```python
# Create and save a collection of training docs
train_docbin = DocBin(docs = train_docs)
train_docbin.to_disk('./train.spacy')
# Create and save a collection of evaluation docs
dev_docbin = DocBin(docs = dev_docs)
dev_docbin.to_disk('./dev.spacy')
```

#### TIPS

* `spacy convert` lets you convert corpora in common formats
* supports `.conll`, `.conllu`, `.iob` and spaCy's old json format

`$ python -m spacy convert ./train.gold.conll ./corpus`
