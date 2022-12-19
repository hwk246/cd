import greenlight

def test_passing():
    assert greenlight.passing(10,20) == 30
    assert greenlight.passing('Winc', 'acadamy') == 'Wincacadamy'