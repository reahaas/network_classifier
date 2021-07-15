from rule_matcher import rule_types_matcher


def communication_match_rule(communication, rule):
    rule_type = rule.type
    rule_match_checker = rule_types_matcher[rule_type]
    
    return rule_match_checker(communication, rule)


def build_classification(communication, rule):
    # todo implement
    return {}


def get_classifications(communication, rules):
    """

    :param tuple communication:  (id (int), timestamp (int), device_id (text), protocol_name (text), host (text))
    :param list(tuple) rules: list of rules
    """
    classifications = []
    for rule in rules:
        if communication_match_rule(communication, rule):
            classification = build_classification(communication, rule)
            classifications += classification
    
    return classifications


def get_single_classifications_for_all_communication(communications, rules):
    """

    :param list(tuple) communications:
    :param list(tuple) rules:
    :return:
    """
    single_classifications = []
    for communication in communications:
        classifications = get_classifications(communication, rules)
        single_classifications += classifications
    return single_classifications
