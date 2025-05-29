import pytest

def test_seed_data():
    seed_data = {"title": "Sample Title", "author": "Sample Author"}
    assert seed_data["title"] == "Sample Title"
    assert seed_data["author"] == "Sample Author"