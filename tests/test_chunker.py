import pytest
from src.chunker import chunk_fixed, validate_arguments

def test_chunk_fixed_empty_string():
    assert chunk_fixed("") == []
    assert chunk_fixed("   ") == []
    assert chunk_fixed("\n\t") == []

# 3. Text shorter than size
def test_text_shorter_than_size():
    text = "hello"
    assert chunk_fixed(text, size=10, overlap=2) == [text]

def test_text_equal_to_size():
    text = "hello"
    assert chunk_fixed(text, size=5, overlap=2) == [text]

def test_text_longer_than_size():
    text = "abcdefghij"
    expected_chunks = ["abcde", "defgh", "fghij"]
    assert chunk_fixed(text, size=5, overlap=2) == expected_chunks

def test_text_with_overlap():
    text = "abcdefghijkl"
    expected_chunks = ["abcde", "defgh", "ghijk","hijkl"]
    assert chunk_fixed(text, size=5, overlap=2) == expected_chunks
    assert chunk_fixed(text, size=5, overlap=0) == ["abcde", "fghij", "hijkl"]

# 7. Last chunk reaches end of text
def test_last_chunk_reaches_end():
    text = "abcdefghijk"
    chunks = chunk_fixed(text, size=4, overlap=1)
    assert chunks[-1][-1] == text[-1]

# 14. Non-string input
@pytest.mark.parametrize(
    "text",
    [
        123,
        None,
        ["hello", "world"],
        {"text": "hello"},
    ],
)
def test_non_string_input(text):
    with pytest.raises(TypeError):
        chunk_fixed(text)

# 16. Unicode
def test_unicode():
    text = "नमस्ते दुनिया 😊 hello"

    chunks = chunk_fixed(text, size=8, overlap=2)

    assert chunks
    assert "".join(chunks) != ""

# 18. Real corpus smoke test
def test_real_corpus():
    from pathlib import Path

    input_file = Path(__file__).parents[1] / "data" / "input.txt"

    text = input_file.read_text(encoding="utf-8")

    chunks = chunk_fixed(text)

    assert len(chunks) > 1
    assert all(len(chunk) <= 1000 for chunk in chunks)

def test_validate_arguments():
    with pytest.raises(ValueError):
        validate_arguments(0, 0)

    with pytest.raises(ValueError):
        validate_arguments(-1, 0)

    with pytest.raises(ValueError):
        validate_arguments(10, -1)

    with pytest.raises(ValueError):
        validate_arguments(10, 10)

@pytest.mark.parametrize(
    "size, overlap",
    [
        (0, 0),      # size <= 0
        (-1, 0),     # size <= 0
        (10, -1),    # overlap < 0
        (10, 10),    # overlap >= size
        (10, 11),    # overlap >= size
    ],
)
def test_validate_arguments(size, overlap):
    with pytest.raises(ValueError):
        validate_arguments(size, overlap)