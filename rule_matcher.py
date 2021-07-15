import ipaddress
import struct
import socket


# credit to: https://stackoverflow.com/a/51472420/8808983
def is_ip_in_network(ip, net):
    """
    Is an ip address in a network
    :param str ip:
    :param net:
    :return:
    """
    return ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(net)


# credit: https://stackoverflow.com/a/15034269/8808983
def get_ips(url):
    """
    This method returns an array containing
    one or more IP address strings that respond
    as the given domain name.
    
    :param str url:
    :return list(str): list of ips as strings.
    """
    try:
        data = socket.gethostbyname_ex(url)
        ips = repr(data[2])
        return ips
    except Exception:
        return []


class RuleMatcher():
    
    @staticmethod
    def is_match_communicating_protocol(communication, rule):
        return communication.protocol_name == rule.argument

    @staticmethod
    def is_match_communicating_with(communication, rule):
        return communication.host == rule.argument

    @staticmethod
    def is_match_communicating_with_subnet(communication, rule):
        return is_ip_in_network(communication.host, rule.argument)

    @staticmethod
    def is_match_communicating_with_domain(communication, rule):
        return communication.host in get_ips(rule.argument)


# this dict is a mapping to get the right rule to use by the rule type
rule_types_matcher = {
        "communicating_protocol": RuleMatcher.is_match_communicating_protocol,
        "communicating_with": RuleMatcher.is_match_communicating_with,
        "communicating_with_subnet": RuleMatcher.is_match_communicating_with_subnet,
        "communicating_with_domain": RuleMatcher.is_match_communicating_with_domain
    }
