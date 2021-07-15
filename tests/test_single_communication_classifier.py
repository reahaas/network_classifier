from data_types import Communication, Rule, Classification
from rule_matcher import rule_types_matcher
from single_communication_clasifier import get_classifications, g_classification_id_generator


def assert_is_rule_match(communication, rule):
    rule_match_checker = rule_types_matcher[rule.type]
    is_rule_match = rule_match_checker(communication, rule)
    assert is_rule_match, f"communication didn't matched the rule: {communication}, {rule}"


class TestSingleCommunicationClassifier():
    

    def setup_method(self):
        """
        This is a pytest method, see: https://code-maven.com/slides/python/pytest-class
        This function run before each of the tests.
        :return:
        """
        g_classification_id_generator.reset(to_value=0)
    
    def test_rule_communicating_protocol(self):
        rule_id = 1
        rule = Rule(rule_id, "communicating_protocol", "http", "user endpoint")
        communication = Communication(1, 1578455846, "aaaa", "http", "10.0.0.1")
        rules = [rule]
    
        assert_is_rule_match(communication, rule)
    
        # test build:
        single_classifications = get_classifications(communication, rules)
        
        expected_classification = [Classification(1, "aaaa", "user endpoint", rule_id)]
        assert single_classifications == expected_classification
    
    
    def test_rule_communicating_with(self):
        rule_id = 1
        rule = Rule(rule_id, "communicating_with", "10.1.1.1", "ct")
        rules = [rule]
        
        communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.1")
    
        assert_is_rule_match(communication, rule)
        
        single_classifications = get_classifications(communication, rules)
        
        expected_classification = [Classification(1, "aaaa", "ct", rule_id)]
        assert single_classifications == expected_classification
    
    
    def test_rule_communicating_with_subnet(self):
        rule_id = 1
        rule = Rule(rule_id, "communicating_with_subnet", "10.1.1.0/24", "ct")
        rules = [rule]
        
        communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
        assert_is_rule_match(communication, rule)
        
        single_classifications = get_classifications(communication, rules)
        
        expected_classification = [Classification(1, "aaaa", "ct", rule_id)]
        assert single_classifications == expected_classification
    
    
    def test_rule_communicating_with_domain(self, mocker):
        mocker.patch('rule_matcher.get_ips', return_value=["10.1.1.8"])
        
        rule_id = 1
        rule = Rule(rule_id, "communicating_with_domain", "www.apple.com", "iphone")
        rules = [rule]
        
        communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.8")
    
        assert_is_rule_match(communication, rule)
        
        single_classifications = get_classifications(communication, rules)
        
        expected_classification = [Classification(1, "aaaa", "iphone", rule_id)]
        assert single_classifications == expected_classification
    
    
    def test_2_rules_one_one_communication(self):
        rule_id_1 = 1
        rule_id_2 = 2
        rule_1 = Rule(rule_id_1, "communicating_with", "10.1.1.1", "ct")
        rule_2 = Rule(rule_id_2, "communicating_with_subnet", "10.1.1.0/24", "ct")
        # rule_2 = Rule(rule_id_2, "communicating_with_domain", "www.google.com", "iphone")
        rules = [rule_1, rule_2]
    
        communication = Communication(1, 1578455846, "aaaa", "ssl", "10.1.1.1")
        
        assert_is_rule_match(communication, rule_1)
        assert_is_rule_match(communication, rule_2)
        
        single_classifications = get_classifications(communication, rules)
        
        expected_classifications = [
            Classification(1, "aaaa", "ct", rule_id_1),
            Classification(2, "aaaa", "ct", rule_id_2)
        ]
        assert set(single_classifications) == set(expected_classifications)
