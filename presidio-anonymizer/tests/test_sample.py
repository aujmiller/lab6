import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    input_text = "My name is Bond"
    start, end = 11, 15
    result = sample_run_anonymizer(input_text, start, end)

    assert result.text == "My name is BIP"
    assert len(result.items) == 1
    item = result.items[0]
    assert item.start == start
    assert item.end == end - 1
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"