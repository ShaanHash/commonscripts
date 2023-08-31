#!/usr/bin/python

import subprocess
import argparse

# Create argument Handler
parser = argparse.ArgumentParser("massnslookup.py file.txt ANY 0.0.0.0:53")

# Define each argument
parser.add_argument("domain_file_path", help="The file-path of the txt file containing newline separated domains", type=str)
parser.add_argument("query", help="ANY, NS, A, AAAA", type=str)
parser.add_argument("target_name_server", help="The domain of the nameserver you would like to query", type=str)

# Capture arguments
args = parser.parse_args()

# Open the file containing the domains
domains = open(args.domain_file_path, "r").readlines()

# Call the nslookup command on each domain
for domain in domains:
    subprocess.run([
        "nslookup",
        "-query={}".format(args.query_type),
        domain.strip(),
        args.target_name_server,
    ])
