import json
from pathlib import Path
from urllib.request import Request, urlopen

API_URL = "https://api.github.com/repos/karpathy/char-rnn/contents/data/tinyshakespeare"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def discover_files():
    request = Request(API_URL, headers={"User-Agent": "rag-eval"})
    with urlopen(request) as response:
        items = json.load(response)

    if not isinstance(items, list):
        raise ValueError(f"Expected a list of repo items from GitHub API, got {type(items).__name__}")

    return [
        item for item in items
        if item.get("type") == "file" and item.get("name", "").endswith(".txt")
    ]


def fetch_and_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    saved_files = []

    for item in discover_files():
        download_url = item["download_url"]
        file_request = Request(download_url, headers={"User-Agent": "rag-eval"})

        with urlopen(file_request) as response:
            content = response.read().decode("utf-8")

        local_path = DATA_DIR / item["name"]
        local_path.write_text(content, encoding="utf-8")
        saved_files.append(str(local_path))

    return saved_files


if __name__ == "__main__":
    print(fetch_and_store())