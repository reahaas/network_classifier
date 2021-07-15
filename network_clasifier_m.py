import csv

from data_types import Communication, Rule
from final_classification_picker import get_final_classifications
from single_communication_clasifier import get_single_classifications_for_all_communication

# todo: define as class and extract to other file.
# global objects:

# "device_id": final_classification
devices = {}

# "classification_id": (timestamp (datetime), rule_id, device_id (text), classification (text))
single_classifications = {}


def read_csv_file_as_data_type(file_path, data_type):
    """

    :param file_path:
    :param class data_type: namedtuple class type, to convert the data to.
    :return list(namedtuple):
    """
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    data_type_list = []
    for line in data:
        data_type_list += data_type(line)

    return data_type_list


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


def read_communications_file(communications_file):
    """

    :param communications_file:
    :return list(Communication):
    """
    return read_csv_file_as_data_type(communications_file, Communication)


def read_communications_file(rules_file):
    """

    :param rules_file:
    :return list(Rule):
    """
    return read_csv_file_as_data_type(rules_file, Rule)
    

def network_classifier(communications_file, rules_file, final_classification_file):
    communications = read_communications_file(communications_file)
    rules = read_csv_file_as_data_type(rules_file)
    
    single_classifications = get_single_classifications_for_all_communication(communications, rules)
    
    final_classifications = get_final_classifications(single_classifications, devices)
    
    report_final_classifications(final_classifications, final_classification_file)
