from BJSS_interview import LBTT_Calculator
import pytest


def test_LBTT_handlezero():
    assert LBTT_Calculator(0) == 0


def test_LBTT_handle_negative():
    with pytest.raises(ValueError):
        LBTT_Calculator(-37)


def test_LBTT_below_first_threshold():
    assert LBTT_Calculator(130000) == 0


def test_LBTT_middle_band():
    assert LBTT_Calculator(500000) == 23350


def test_LBTT_above_max_threshold():
    assert LBTT_Calculator(1000000) == 78350
