## Decision
Default size = 1000 
Default overlap = 200
Return type = list[str]
whitespace in chunks = slice raw
tail chunk - back up final chunks to the end of text
bad arguments - raise 

## Phase 6 — Real Corpus Observation

Ran the fixed-size chunker on the original `data/input.txt` corpus.

- Number of chunks: 1394
- Chunk size: 1000 characters
- Overlap: 200 characters
- Maximum chunk length observed: 1000 characters
- The overlap between consecutive chunks was verified to be 200 characters.
- Fixed-size character chunking can split words or sentences at arbitrary character boundaries.
- This is a limitation of character-based chunking and will be useful for comparison with structure-aware chunking later.