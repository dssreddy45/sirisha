# Tokenization Experiment Report

## 1. Objective

This experiment examines how a Hugging Face tokenizer breaks text into tokens, converts those tokens into numeric IDs, and decodes the IDs back into text. It also compares how token counts differ across three text types of varying length and structure: a short sentence, a long paragraph, and a snippet of programming code.

## 2. Tokenizer Used

- **Model:** `bert-base-uncased`
- **Algorithm:** WordPiece (subword-based)
- **Vocabulary size:** ~30,522 tokens
- **Loaded via:** `transformers.AutoTokenizer.from_pretrained("bert-base-uncased")`

## 3. Methodology

1. Load the pretrained tokenizer.
2. For each sample text, call `tokenizer.tokenize()` to split it into subword tokens.
3. Convert the tokens into numeric IDs with `tokenizer.convert_tokens_to_ids()`.
4. Decode the IDs back into text with `tokenizer.decode()` to confirm the process is reversible.
5. Record the token count for each sample and compare the three text types.

## 4. Test Inputs

**Short Sentence** (6 words)
> Tokenization breaks text into smaller units.

**Long Paragraph** (87 words)
> Tokenization is the process of splitting text into smaller pieces, called tokens, before feeding it into a machine learning model. Modern transformer models like BERT and GPT use subword tokenization, which breaks rare or unknown words into smaller, more common pieces. This approach helps the model handle a much larger vocabulary than word-level tokenization while keeping the total number of unique tokens manageable. As a result, even words the model has never seen during training can often still be represented as a sequence of familiar subword units.

**Programming Code** (14 words/identifiers)
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## 5. Results

| Text Type | Word Count | Token Count | Tokens per Word |
|---|---|---|---|
| Short Sentence | 6 | *(fill in from script output)* | *(—)* |
| Long Paragraph | 87 | *(fill in from script output)* | *(—)* |
| Programming Code | 14 | *(fill in from script output)* | *(—)* |

> **Note:** Run `tokenization_experiment.py` in Google Colab and copy the printed "Token count" line for each sample into this table. This environment can't reach the Hugging Face hub to download the model directly, so the live counts come from your Colab run.

## 6. Observations

A WordPiece tokenizer rarely maps one word to exactly one token. Longer or less common words get split into a root piece plus continuation pieces (marked with `##`), so the token count for natural-language text is typically somewhat higher than the raw word count.

Code tends to tokenize less efficiently than prose. Identifiers, indentation, and symbols like `==` or `(` weren't part of BERT's original training distribution (which was mostly English Wikipedia and book text), so the tokenizer often breaks variable names and operators into multiple smaller pieces rather than recognizing them as single units.

The long paragraph and short sentence both draw from everyday English vocabulary, so their tokens-per-word ratio should stay closer to 1, while the code snippet's ratio is expected to run noticeably higher for the reasons above.

## 7. Conclusion

Subword tokenization lets a single, fixed-size vocabulary represent virtually any input text, including words never seen during training, by decomposing them into familiar fragments. How efficiently a given vocabulary handles a piece of text depends heavily on how closely that text resembles the tokenizer's original training data — general English sentences and paragraphs tokenize cleanly, while domain-specific content like source code incurs a higher token cost per unit of meaning.
