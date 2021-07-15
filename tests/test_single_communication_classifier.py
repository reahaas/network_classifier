from single_communication_clasifier import get_classifications


def test_rule_communicating_protocol():
    rule = {1, "communicating_protocol", "http", "user endpoint"}
    communication = (1, 1578455846, "aaaa", "http", "10.0.0.1")
    rules = [rule]
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [(1, "aaaa", "user endpoint")]
    assert single_classifications == expected_classification


def test_rule_communicating_with():
    rule = {1, "communicating_with", "10.1.1.1", "ct"}
    rules = [rule]
    
    communication = (1, 1578455846, "aaaa", "ssl", "10.1.1.1")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [(1, "aaaa", "ct")]
    assert single_classifications == expected_classification


def test_rule_communicating_with_subnet():
    rule = {1, "communicating_with_subnet", "10.1.1.0/24", "ct"}
    rules = [rule]
    
    communication = (1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [(1, "aaaa", "ct")]
    assert single_classifications == expected_classification


def test_rule_communicating_with_domain():
    rule = {1, "communicating_with_domain", "www.apple.com", "iphone"}
    rules = [rule]
    
    communication = (1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classification = [(1, "aaaa", "iphone")]
    assert single_classifications == expected_classification


def test_2_rules_one_one_communication():
    rule_1 = rule = {1, "communicating_with_subnet", "10.1.1.0/24", "ct"}
    rule_2 = rule = {2, "communicating_with_domain", "www.apple.com", "iphone"}
    rules = [rule_1, rule_2]
    
    communication = (1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
    single_classifications = get_classifications(communication, rules)
    
    expected_classifications = [(1, "aaaa", "ct"), (2, "aaaa", "iphone")]
    assert set(single_classifications) == set(expected_classifications)
