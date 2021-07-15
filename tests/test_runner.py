import os

from data_types import Classification
from network_clasifier_m import network_classifier, read_classifications_file


def assert_file_exists(file_path):
    assert os.path.isfile(file_path)


def test_main():
    communications_file = "data/communications.csv"
    rules_file = "data/rules.csv"
    final_classification_file = "data/final_classification.csv"
    
    network_classifier(communications_file, rules_file, final_classification_file)
    
    assert_file_exists(final_classification_file)

    expected_classification = [Classification(1, "aaaa", "user endpoint", 1)]
    
    classifications_from_file = read_classifications_file("data/final_classification_all_classifications.csv")
    classifications = fix_int_fields_in_classifications(classifications_from_file)

    assert classifications == expected_classification


def fix_int_fields_in_classifications(classifications_from_file):
    classifications = []
    for classification in classifications_from_file:
        fixed_classification = Classification(
            int(classification.id),
            classification.device_id,
            classification.classification,
            int(classification.rule_id)
        )
        classifications.append(fixed_classification)
    return classifications
