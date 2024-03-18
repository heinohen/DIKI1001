# Configuring and running the training

## Training config

* Single source of truth for all settings
* Typically called `config.cfg`
* Defines how to initialize the `nlp` object
* Includes all settings about the pipeline components and their model implementations
* Configures the training process and hyperparameters
* Makes your training more reproducible

``` python
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
```

## Generating a config

* spaCy can auto-generate a defaultr config file for you
* interactive [quickstart](https://spacy.io/usage/training#quickstart) widget in the docs

* init config command on the CLI

`python -m spacy init config ./config.cfg --lang en --pipeline ner`

* `init config` the command to run
* `config.cfg` output path for the generated config
* `--lang` language class of the pipeline, eg `en` for english
* `--pipeline` comma-separated names of components to include

All you need is the `config.cfg` and the training and development data.

* Config settings can be overwritten on the command line

`$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy`

* `train` the command to run
* `config.cfg`the path to the config file
* `--output` the path to the output dir to save the trained pipeline
* `--paths.train` override with path to the training data
* `--paths.dev` override with path to the evaluation data

## Loading a trained pipeline

* output after training is a regural loadable spaCy pipeline
  * `model-last` last trained pipeline
  * `model-best` best trained pipeline

* load it with `spacy.load`

```python
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)
```

### TIP: packaging your pipeline

* [spacy package](https://spacy.io/api/cli#package) create an installable Python package containing your pipeline
* easy to version and deploy

``` bash
python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
cd ./packages/en_my_pipeline-1.0.0
pip install dist/en_my_pipeline-1.0.0.tar.gz

```

Load and use `nlp = spacy.load("en_my_pipeline")`
