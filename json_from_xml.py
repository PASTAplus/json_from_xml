#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import click
import json

from metapype.model import metapype_io, mp_io
from metapype.model.node import Node


@click.command()
@click.argument('input_file')
def json_from_xml(input_file: str):
    """
    Generates a Metapype model JSON file from an EML file. This JSON file is suitable for ezEML input.

Arguments: \n
        INPUT_FILE: Name of XML file containing an EML metadata document, with full path \n

        The output JSON file will have the same basename as the input file and will be written into the same directory. \n
    """
    # Check the Python version
    if (sys.version_info < (3, 7)):
        print('Requires Python 3.7 or later')
        exit(0)

    main(input_file)


# def to_json(node: Node, indent: int = 1) -> str:
#     """
#     Converts a Metapype model instance to JSON
#
#     Args:
#         indent:
#         node: node of the model instance
#
#     Returns:
#         str: JSON of Metapype model instance
#
#     """
#     j = _serialize(node)
#     return json.dumps(j, indent=indent)


def _json_from_xml(filename):
    xml = None
    if not filename.lower().endswith('.xml'):
        print('Input file must have .xml extension. Exiting.')
        exit(0)
    try:
        with open(f"{filename}", "r") as f:
            xml = "".join(f.readlines())
    except FileNotFoundError:
        print('Input file not found. Exiting.')
        exit(0)
    eml = metapype_io.from_xml(xml)
    if not isinstance(eml, Node):
        print('Metapype failed to validate the XML input. Exiting.')
        exit(0)
    # return mp_io.to_json(eml)
    return metapype_io.to_json(eml)
    # _json = metapype_io.to_json(eml)
    # parsed = json.loads(_json)
    # return json.dumps(parsed, indent=1, sort_keys=False)


def main(input_filename: str):
    _json = _json_from_xml(input_filename)
    output_filename = input_filename[:-4] + '.json'
    with open(output_filename, 'w') as output_file:
        output_file.write(_json)
    print('Done. Exiting.')


if __name__ == '__main__':
    # main('/Users/jide/Downloads/NTL_people_sites_template.xml')
    json_from_xml()
