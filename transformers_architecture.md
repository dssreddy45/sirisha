# Transformer Architecture

---

## 1. Evolution of NLP

### Rule-Based Systems
- Used hand-written grammar rules and dictionaries to process text
- Linguists manually defined every rule for parsing language
- Could not handle ambiguity, slang, or new words

### Machine Learning NLP
- Statistical models learned patterns from labeled text data
- Algorithms like Naive Bayes and SVM became popular
- Still required manual feature engineering

### Deep Learning NLP
- RNNs and LSTMs processed text sequentially word by word
- Word embeddings like Word2Vec captured meaning of words
- Struggled with long sentences and could not be parallelized

### Transformer-Based NLP
- Google introduced Transformer in 2017 with Attention Is All You Need
- Processes entire sentences at once using attention mechanism
- Powers all modern LLMs like BERT, GPT, Claude, and ChatGPT

---

## 2. Transformer Components

### Encoder
- Reads and understands the entire input text
- Converts input tokens into rich contextual representations
- Used in BERT for classification and question answering tasks

### Decoder
- Generates output text one word at a time
- Looks at encoder output while generating each word
- Used in GPT for text generation tasks

### Self-Attention
- Allows each word to look at all other words simultaneously
- Captures relationships and dependencies between words
- Solves the long-range dependency problem of RNNs

### Multi-Head Attention
- Runs multiple self-attention operations in parallel
- Each head learns different relationships like grammar and meaning
- Outputs are combined for richer understanding of text

### Positional Encoding
- Adds information about position of each word in sentence
- Uses sine and cosine functions to create unique position patterns
- Without it the model cannot distinguish word order

### Feed Forward Neural Network
- Applied to each position after the attention layer
- Learns complex non-linear patterns attention cannot capture
- Has two linear layers with ReLU activation in between

### Residual Connections
- Adds the input of a layer directly to its output
- Solves the vanishing gradient problem in deep networks
- Makes training very deep Transformer models possible

### Layer Normalization
- Normalizes activations within each layer
- Stabilizes training and keeps activations in consistent range
- Makes training faster and less sensitive to learning rate

---
