from collections import namedtuple

Communication = namedtuple("Communication", "id timestamp device_id protocol_name host")

Rule = namedtuple("Rule", "id type argument classification")

Classification = namedtuple("Classification", "id device_id classification")
