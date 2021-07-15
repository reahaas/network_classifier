from data_types import Classification
from rule_matcher import rule_types_matcher


class ClassificationIdGenerator():
    def __init__(self):
        self.id_counter = 0
    
    def next(self):
        self.id_counter += 1
        return self.id_counter
    
    def reset(self, to_value=0):
        self.id_counter = to_value


g_classification_id_generator = ClassificationIdGenerator()


def communication_match_rule(communication, rule):
    rule_type = rule.type
    rule_match_checker = rule_types_matcher[rule_type]
    
    return rule_match_checker(communication, rule)


def build_classification(communication, rule):
    return Classification(
        g_classification_id_generator.next(),
        communication.device_id,
        rule.classification,
        rule.id
    )


def get_classifications(communication, rules):
    """

    :param Communication communication:  (id (int), timestamp (int), device_id (text), protocol_name (text), host (text))
    :param list(Rules) rules: list of rules
    """
    classifications = []
    for rule in rules:
        if communication_match_rule(communication, rule):
            classification = build_classification(communication, rule)
            classifications.append(classification)
    
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
