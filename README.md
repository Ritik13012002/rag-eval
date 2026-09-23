# RAG Evaluation

A hand-written fixed-size text chunker implemented in Python for evaluating
chunking behavior on a real text corpus.

## Current implementation

The project currently includes a fixed-size character chunker with:

- 1000-character chunks
- 200-character overlap
- Input validation
- Deterministic output
- Pytest test coverage

## Corpus

The original corpus is stored in `data/input.txt`.

For experimentation, the corpus was also divided into 50 files,
with 800 lines per file.

## Observation

Fixed-size character chunking maintains the requested overlap, but it can
split words or sentences at arbitrary character boundaries.