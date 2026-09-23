from typing import Final

DEFAULT_SIZE: Final[int] = 1000
DEFAULT_OVERLAP: Final[int] = 200

#validate the arguments for chunk size and overlap
def validate_arguments(size:int, overlap:int):
    if size <= 0:
        raise ValueError("Chunk should be greater than 0")
    if overlap < 0:
        raise ValueError("Chunk overlap should be greater than or equal to 0")
    if overlap >= size:
        raise ValueError("Chunk overlap should be less than chunk size")
def chunk_fixed(text:str , size:int=DEFAULT_SIZE , overlap:int = DEFAULT_OVERLAP)->list[str]:
    validate_arguments(size, overlap)
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.strip():
        return []
    step = size - overlap
    chunks=[]
    for i in range (0,len(text),step):
        if i + size >= len(text):
            i = max(0 , len(text)-size)
            chunk = text[i:len(text)]
            chunks.append(chunk)
            break
        else:
            chunk = text[i:i+size]
            chunks.append(chunk)
    return chunks

