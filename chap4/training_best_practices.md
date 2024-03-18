# Training best practices

## Problem 1: Models can "forget" things

* Existing model can overfit on new data
  * e.g. if you onyl update it with `"WEBSITE"`, it can unlearn what `"PERSON"` is.
  * Also known as "catastrophic forgetting" problem

### Solution

* Mix in previously correct predictions
  * For example if you're training `"WEBSITE"` also include examples of `"PERSON"`
  * Run existing spaCy model over adata and extract all other relevant entities

## Problem 2: Models can't learn everything

* spaCy's models make predictions based on _local context_
* Models can struggle to learn if decision is difficult to make based on context
* Label scheme needs to be consistent and not too specific
  * For example `"CLOTHING"` is better than `"ADULT_CLOTHING"`and `"CHILDRENS_CLOTHING"`

### Solution Plan your label scheme carefully

* Pick categories that are reflected in local context
* More generic is better than too specific
* Use rules to go from generic labels to specific categories

#### BAD

``` python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

#### GOOD

``` python
LABELS = ["CLOTHING", "BAND"]
```