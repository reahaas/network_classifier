import argparse

from network_clasifier_m import network_classifier


def get_command_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-c", "--communications_file", help="input file for communications")
    parser.add_argument("-r", "--rules_file", help="input file for rules")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_command_args()
    network_classifier(args.communications_file, args.rules_file)
