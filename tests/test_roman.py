import pytest
from normalize_kor import kormalize


def test_words():
    """
    This tests that words get romanized in a correct way!
    """
    test_words = [("화이팅!", "hwaiting!"), ("잘할 수 있어요!", "jalhal su isseoyo!"), ("병원에", "byeongwone"),
                  ("저기요", "jeogiyo"), ("고맙습니다", "gomapseumnida")]

    for t in test_words:
        assert t[1] == kormalize(t[0]) 


def test_special():
    """
    This tests that words get romanized in a correct way!
    """
    test_words = [("몰라요", "mollayo"), ]

    for t in test_words:
        assert kormalize(t[0]) == t[1]