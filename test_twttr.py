import pytest

from twttr import shorten


def test_shorten_word():
    assert shorten("menaka") == "mnk"


def test_shorten_words():
    assert shorten("hello, menaka") == "hll, mnk"


def test_shorten_no_vowels():
    assert shorten("cry") == "cry"


def test_shorten_caps():
    assert shorten("Menaka") == "Mnk"


def test_shorten_blank():
    assert shorten("") == ""


def test_shorten_spaces():
    assert shorten("    ") == "    "


def test_shorten_punctuation():
    assert shorten("a.e!i?o,u") == ".!?,"


def test_shorten_with_numbers():
    assert shorten("a1e2i3o4u5") == "12345"


def test_shorten_type_error():
    with pytest.raises(TypeError):
        shorten()

    with pytest.raises(TypeError):
        shorten(1)

    with pytest.raises(TypeError):
        shorten(0.5)
