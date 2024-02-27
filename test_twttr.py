from twttr import remove_vowels

def test_remove_vowels():
    assert remove_vowels("a") == ""
    assert remove_vowels("") == ""
    assert remove_vowels("aa") == ""
    assert remove_vowels("aae") == ""
    assert remove_vowels("asdfghjklu") == "sdfghjkl"
    assert remove_vowels("auieo") == ""
    assert remove_vowels("a href") == " hrf"
    assert remove_vowels("uipoa") == "p"
    assert remove_vowels(" ") == " "
    assert remove_vowels(" aa hds a a l d") == "  hds   l d"

test_remove_vowels()