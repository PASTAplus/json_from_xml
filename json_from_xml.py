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
    return metapype_io.to_json(eml)


def main(input_filename: str):
    _json = _json_from_xml(input_filename)
    output_filename = input_filename[:-4] + '.json'
    with open(output_filename, 'w') as output_file:
        output_file.write(_json)
    print('Success')


if __name__ == '__main__':
    json_from_xml()
