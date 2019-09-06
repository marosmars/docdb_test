import pprint

from pymongo import MongoClient

services_sample_2 = {
    "timestamp": 2,
    "services": [
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/15",
                    "remote_ip": "UNKNOWN",
                    "vlan": 1501
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.100",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "CPE-Test",
            "vccid": 1501
        }
    ]
}

services_sample = {
    "timestamp": 1,
    "services": [
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/15",
                    "remote_ip": "UNKNOWN",
                    "vlan": 1501
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.100",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "CPE-Test",
            "vccid": 1501
        },
        {
            "devices": [
                {
                    "id": "B100",
                    "interface": "ethernet 2/2",
                    "remote_ip": "213.143.100.100",
                    "vlan": 2000
                },
                {
                    "id": "B21",
                    "interface": "ethernet 4/2",
                    "remote_ip": "213.143.100.21",
                    "vlan": 2000
                }
            ],
            "id": "MAGENTATEST",
            "vccid": 8888
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 3118
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 3118
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.25",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-APMgmt-MI",
            "vccid": 459
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 3123
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-APMgmt-SIM",
            "vccid": 67
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 3127
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 3127
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.15",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-APMgmt-SUED",
            "vccid": 461
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 103
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 103
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Alarmanl",
            "vccid": 339
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 2/13",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 60
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 60
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 60
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.8",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.25",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.107",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.13",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.15",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.11",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.24",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.5",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-DMZ",
            "vccid": 338
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 25
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 25
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Mgmt-Etherlink",
            "vccid": 460
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 18
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 18
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.25",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Mgmt-MI",
            "vccid": 457
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 118
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 118
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.25",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Mgmt-MI-2",
            "vccid": 458
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 23
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Mgmt-SIM",
            "vccid": 98
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 27
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 27
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.15",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-Mgmt-SUED",
            "vccid": 462
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 130
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 130
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.25",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.8",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.11",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.107",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.13",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.15",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.5",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.24",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN-blizz-BB",
            "vccid": 328
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 100
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 100
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN_LS",
            "vccid": 483
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 101
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 101
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN_LS_DN2",
            "vccid": 484
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 200
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 200
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN_VW",
            "vccid": 485
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 1/13",
                    "remote_ip": "UNKNOWN",
                    "vlan": 201
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/14",
                    "remote_ip": "UNKNOWN",
                    "vlan": 201
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "WBN_VW_DN2",
            "vccid": 486
        },
        {
            "devices": [
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/17",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 5
                },
                {
                    "id": "B21",
                    "interface": "ethernet 2/6",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 5
                },
                {
                    "id": "B28",
                    "interface": "ethernet 1/14",
                    "remote_ip": "213.143.100.28",
                    "untagged": True,
                    "vlan": 5
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.21",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B100",
                    "interface": "ethernet 1/5",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 5
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.6",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B21",
                    "interface": "ethernet 2/8",
                    "remote_ip": "UNKNOWN",
                    "untagged": True,
                    "vlan": 5
                }
            ],
            "id": "WLAN-AP-Management",
            "vccid": 687
        },
        {
            "devices": [
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.8",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.22",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.9",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.14",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.1",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.15",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.27",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B100",
                    "interface": "ethernet 1/24",
                    "remote_ip": "UNKNOWN",
                    "vlan": 11
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.7",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.18",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.10",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B28",
                    "interface": "ethernet 1/2",
                    "remote_ip": "213.143.100.11",
                    "vlan": 11
                },
                {
                    "id": "B28",
                    "interface": "ethernet 1/14",
                    "remote_ip": "213.143.100.11",
                    "vlan": 11
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.21",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.13",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B21",
                    "interface": "ethernet 2/16",
                    "remote_ip": "UNKNOWN",
                    "vlan": 11
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.107",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B21",
                    "interface": "ethernet 1/2",
                    "remote_ip": "UNKNOWN",
                    "vlan": 11
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.6",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.3",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.16",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.12",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.19",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.20",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "managementvpls",
            "vccid": 12
        },
        {
            "devices": [
                {
                    "id": "B21",
                    "interface": "ethernet 2/4",
                    "remote_ip": "213.143.100.21",
                    "vlan": 101
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.8",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "B28",
                    "interface": "ethernet 1/19",
                    "remote_ip": "213.143.100.14",
                    "untagged": True,
                    "vlan": 101
                },
                {
                    "id": "B28",
                    "interface": "ethernet 1/18",
                    "remote_ip": "213.143.100.14",
                    "untagged": True,
                    "vlan": 101
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.26",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.6",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                },
                {
                    "id": "UNKNOWN",
                    "interface": "UNKNOWN",
                    "remote_ip": "213.143.100.23",
                    "untagged": "UNKNOWN",
                    "vlan": "UNKNOWN"
                }
            ],
            "id": "secure-mgmt-vlan101",
            "vccid": 1113
        }
    ]
}

client = MongoClient()
db = client.mydb
db.vpls.drop()

new_vpls_id = db.vpls.insert_one(services_sample).inserted_id
print new_vpls_id
new_vpls_id = db.vpls.insert_one(services_sample_2).inserted_id
print new_vpls_id

# Get entire document based on timestamp
read_services = db.vpls.find_one({"timestamp": 1})
pprint.pprint(read_services)

for i in db.vpls.find(filter={}, projection={"timestamp": 1, "_id": 0}):
    pprint.pprint(i)
print()


# Get entire document based on timestamp
read_services = db.vpls.find_one({"timestamp": 1})
pprint.pprint(read_services)
print()


print("Get names of services in a specific timestamp")
read_services = db.vpls.find_one({"timestamp": 1}, projection={"services.id": 1})
pprint.pprint(read_services)
print()


print("Get all timestamps which contain a specific service")
for i in db.vpls.find(filter={"services.id": "CPE-Test"}, projection={"timestamp": 1}):
    pprint.pprint(i)
print()


print("Get a specific service in specific timestamp")
for i in db.vpls.aggregate([
    {"$match": {"timestamp": 1}},
    {"$project": {
        "services": {
            "$filter": {
                "input": "$services",
                "as": "service",
                "cond": {"$eq": ["$$service.id", "CPE-Test"]}
            },
        }
    }},
    {"$unwind": "$services"}
]):
    pprint.pprint(i)
print()


print("Get names of services in a specific timestamp within a certain vccid")
for i in db.vpls.aggregate([
    {"$match": {"timestamp": 1}},
    {"$project": {
        "timestamp": 1,
        "services": {
            "$filter": {
                "input": "$services",
                "as": "service",
                "cond": {"$gte": ["$$service.vccid", 1501]}
            },
        }
    }},
    {"$project": {
        "timestamp": 1,
        "services.id": 1
    }
    },
    {"$unwind": "$services"}
]):
    pprint.pprint(i)
print()


print("Get a device object under a specific service in a specific timestamp")
for i in db.vpls.aggregate([
    {"$match": {"timestamp": 1}},
    {"$project": {
        "timestamp": 1,
        "services": {
            "$filter": {
                "input": "$services",
                "as": "service",
                "cond": {"$eq": ["$$service.id", "CPE-Test"]}
            },
        }
    }},
    {"$unwind": "$services"},
    {"$project": {
        "services.devices": {
            "$filter": {
                "input": "$services.devices",
                "as": "device",
                "cond": {"$eq": ["$$device.id", "B21"]}
            },
        }
    }}
]):
    pprint.pprint(i)
print()