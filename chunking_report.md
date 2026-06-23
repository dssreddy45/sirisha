# Chunking Strategy Report

## Pipeline
## Results

| Strategy | Chunks | Avg Len | Min | Max |
|----------|--------|---------|-----|-----|
| Small   (256/32,  recursive) | 18 | 198.4 | 61 | 256 |
| Medium  (512/64,  recursive) ✅ BEST | 10 | 371.2 | 112 | 512 |
| Large   (1024/128,recursive) | 6 | 581.3 | 210 | 1024 |
| HiOverlap(512/256,recursive) | 14 | 348.6 | 112 | 512 |
| NoOverlap(512/0,  recursive) | 9 | 382.1 | 98 | 512 |
| CharSplit(512/64, character) | 8 | 401.5 | 134 | 512 |

## Strategy Descriptions

### Small (256/32, Recursive)
- Most chunks, very short text per chunk
- Good for narrow factual queries
- Risk: single idea split across chunks, loses context

### Medium (512/64, Recursive) ✅ BEST
- Holds 1-2 full paragraphs per chunk
- 64-char overlap prevents boundary sentence loss
- Fits all common embedding models (100-130 tokens)
- Best balance of context, precision, and cost

### Large (1024/128, Recursive)
- Fewest chunks, multiple paragraphs each
- Good for summarisation or large-context LLMs
- Risk: retrieval returns too much text, low precision

### Hi-Overlap (512/256, Recursive)
- 50% overlap — no boundary information lost
- Doubles storage and embedding cost
- Returns near-duplicate chunks in retrieval

### No-Overlap (512/0, Recursive)
- Minimum storage — no repeated content
- Risk: sentences cut at boundaries, context lost
- Best when storage cost matters most

### Char Split (512/64, Character)
- Splits strictly on paragraph breaks
- Uneven chunk sizes depending on paragraph length
- Good for well-structured documents

## Winner: Medium Recursive (512 / 64)

| Reason | Detail |
|--------|--------|
| Semantic completeness | 512 chars = 1-2 paragraphs, preserves full idea |
| Retrieval precision | Tighter than large chunks, more focused results |
| Overlap sweet spot | 64 chars prevents loss without doubling storage |
| Model compatibility | Fits all embedding models (100-130 tokens) |
| Cost efficient | Moderate chunk count, low embedding cost |

## When to Use Others

| Use Case | Strategy |
|----------|----------|
| Narrow factual QA | Small (256/32) |
| Summarisation / large LLMs | Large (1024/128) |
| No boundary loss allowed | HiOverlap (512/256) |
| Minimise storage at scale | NoOverlap (512/0) |
| Consistent paragraph structure | CharSplit (512/64) |

## Embedding Model
- Model: sentence-transformers/all-MiniLM-L6-v2
- Vector Dimensions: 384
- Max Tokens: 256
- Normalization: Enabled

## Conclusion
Medium Recursive (512 chars, 64 overlap) is the best default strategy
for RAG pipelines — balancing semantic completeness, retrieval precision,
model compatibility, and cost.
