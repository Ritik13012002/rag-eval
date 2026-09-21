from text_stats import unique_word_count, word_count , clean_text , load_text
def test_empty_string():
    assert word_count("")== 0

def test_word_count():
    assert word_count("hello world") == 2

def test_word_count_with_punctuation():
    assert word_count("!...,") == 0

def test_word_count_with_mixed_case():
    assert word_count("PYTHON python Python Hello") == 4
    assert unique_word_count("PYTHON python Python Hello") == 2
    assert word_count(" ") == 0

def test_load_test(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello Python 😊", encoding="utf-8")
    assert load_text(file) == "Hello Python 😊"
