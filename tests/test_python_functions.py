from survey.python_functions import apply_screener_criterion
import pytest


# Test apply_screener_criterion


def test_apply_screener_criterion_agree_disagree():
    # Test when answer to question 6 is 'agree' and question 7 is 'disagree'
    assert apply_screener_criterion('agree', 'disagree') == True

def test_apply_screener_criterion_agree_agree():
    # Test when both answers are 'agree'
    assert apply_screener_criterion('agree', 'agree') == True

def test_apply_screener_criterion_disagree_disagree():
    # Test when both answers are 'disagree'
    assert apply_screener_criterion('disagree', 'disagree') == True

def test_apply_screener_criterion_disagree_agree():
    # Test when answer to question 6 is 'disagree' and question 7 is 'agree'
    assert apply_screener_criterion('disagree', 'agree') == False

def test_apply_screener_criterion_agree_anything_else():
    # Test when question 6 is 'agree' and question 7 is anything other than 'disagree'
    assert apply_screener_criterion('agree', 'neutral') == True

def test_apply_screener_criterion_disagree_anything_else():
    # Test when question 6 is 'disagree' and question 7 is anything other than 'agree'
    assert apply_screener_criterion('disagree', 'neutral') == False


def test_apply_screener_criterion_anything_disagree():
    # Test when question 7 is 'disagree' and question 6 is anything other than 'agree'
    assert apply_screener_criterion('neutral', 'disagree') == True
  