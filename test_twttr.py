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
