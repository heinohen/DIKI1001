# Generating a config file

Use spaCy’s init config command to auto-generate a config for an English pipeline.
Save the config to a file config.cfg.
    Use the --pipeline argument to specify one pipeline component, ner.

```bash
python -m spacy init config ./config.cfg --lang en --pipeline ner
```

Let’s use the config file generated in the previous exercise and the training corpus we’ve created to train a named entity recognizer!

