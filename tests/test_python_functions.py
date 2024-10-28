from survey.python_functions import apply_screener_criterion, calculate_time_spent
import pytest
from datetime import datetime, timedelta


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



# Test calculate_time_spent


def test_calculate_time_spent_same_time():
    time_str = "2023-04-15 10:00:00"
    assert calculate_time_spent(time_str, time_str) == "00:00"

def test_calculate_time_spent_one_minute():
    start_time = "2023-04-15 10:00:00"
    end_time = "2023-04-15 10:01:00"
    assert calculate_time_spent(start_time, end_time) == "01:00"

def test_calculate_time_spent_one_hour():
    start_time = "2023-04-15 10:00:00"
    end_time = "2023-04-15 11:00:00"
    assert calculate_time_spent(start_time, end_time) == "60:00"

def test_calculate_time_spent_complex():
    start_time = "2023-04-15 10:15:30"
    end_time = "2023-04-15 11:47:15"
    assert calculate_time_spent(start_time, end_time) == "91:45"

def test_calculate_time_spent_across_days():
    start_time = "2023-04-15 23:55:00"
    end_time = "2023-04-16 00:05:00"
    assert calculate_time_spent(start_time, end_time) == "10:00"

def test_calculate_time_spent_invalid_format():
    with pytest.raises(ValueError):
        calculate_time_spent("2023-04-15", "2023-04-16")





  