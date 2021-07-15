from data_types import Communication, Rule, Classification
from single_communication_clasifier import get_classifications


def test_rule_communicating_protocol():
    rule = Rule(1, "communicating_protocol", "http", "user endpoint")
    communication = Communication(1, 1578455846, "aaaa", "http", "10.0.0.1")
    rules = [rule]
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [Classification(1, "aaaa", "user endpoint")]
    assert single_classifications == expected_classification


def test_rule_communicating_with():
    rule = Rule(1, "communicating_with", "10.1.1.1", "ct")
    rules = [rule]
    
    communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.1")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [Classification(1, "aaaa", "ct")]
    assert single_classifications == expected_classification


def test_rule_communicating_with_subnet():
    rule = Rule(1, "communicating_with_subnet", "10.1.1.0/24", "ct")
    rules = [rule]
    
    communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [Classification(1, "aaaa", "ct")]
    assert single_classifications == expected_classification


def test_rule_communicating_with_domain():
    rule = Rule(1, "communicating_with_domain", "www.apple.com", "iphone")
    rules = [rule]
    
    communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [Classification(1, "aaaa", "iphone")]
    assert single_classifications == expected_classification


def test_2_rules_one_one_communication():
    rule_1 = Rule(1, "communicating_with_subnet", "10.1.1.0/24", "ct")
    rule_2 = Rule(2, "communicating_with_domain", "www.apple.com", "iphone")
    rules = [rule_1, rule_2]
    
    communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classifications = [Classification(1, "aaaa", "ct"), Classification(2, "aaaa", "iphone")]
    assert set(single_classifications) == set(expected_classifications)
