
class RuleMatcher():
    
    @staticmethod
    def is_match_communicating_protocol(communication, rule):
        pass

    @staticmethod
    def is_match_communicating_with(communication, rule):
        pass

    @staticmethod
    def is_match_communicating_with_subnet(communication, rule):
        pass

    @staticmethod
    def is_match_communicating_with_domain(communication, rule):
        pass


# this dict is a mapping to get the right rule to use by the rule type
rule_types_matcher = {
        "communicating_protocol": RuleMatcher.is_match_communicating_protocol,
        "communicating_with": RuleMatcher.is_match_communicating_with,
        "communicating_with_subnet": RuleMatcher.is_match_communicating_with_subnet,
        "communicating_with_domain": RuleMatcher.is_match_communicating_with_domain
    }
