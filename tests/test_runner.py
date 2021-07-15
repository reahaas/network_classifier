import os

from network_clasifier_m import network_classifier


def assert_file_exists(file_path):
    assert os.path.isfile(file_path)


def test_main():
    communications_file = "data/communications.csv"
    rules_file = "data/rules.csv"
    final_classification_file = "data/final_classification.csv"
    
    network_classifier(communications_file, rules_file, final_classification_file)
    
    assert_file_exists(final_classification_file)
