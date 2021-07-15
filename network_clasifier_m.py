import csv

from final_classification_picker import get_final_classifications
from single_communication_clasifier import get_single_classifications

# todo: define as class and extract to other file.
# global objects:

# "device_id": final_classification
devices = {}

# "classification_id": (timestamp (datetime), rule_id, device_id (text), classification (text))
single_classifications = {}


def read_csv_file(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def write_csv_file(final_classification_file, final_classifications):
    """

    :param str final_classification_file: file name to write the results to.
    :param list(dict) final_classifications:
    """
    output_file = final_classification_file
    
    if not single_classifications:
        with open(output_file, "w") as my_empty_csv:
            # now you have an empty file already
            pass  # or write something to it already
        return
    
    keys = final_classifications[0].keys()
    with open(output_file, 'w', newline='') as f:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(final_classifications)


def report_final_classifications(final_classifications, final_classification_file):
    # for debbuging
    print(final_classifications)
    print(f"Final classification count: {len(final_classifications)}")
    
    write_csv_file(final_classification_file, final_classifications)


def network_classifier(communications_file, rules_file, final_classification_file):
    communications = read_csv_file(communications_file)
    rules = read_csv_file(rules_file)
    
    single_classifications = get_single_classifications(communications, rules)
    
    final_classifications = get_final_classifications(single_classifications, devices)
    
    report_final_classifications(final_classifications, final_classification_file)
