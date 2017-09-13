import mdc

def test_mdc():
    assert mdc.mdc(48,30) == 6
    assert mdc.mdc(32,20) == 4
    assert mdc.mdc(125,83) == 1