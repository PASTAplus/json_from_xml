# json_from_xml
Tool for converting an EML XML file to Metapype's JSON format, suitable for use as an ezEML template.

The following instructions apply to Linux and MacOS systems. Windows instructions will be forthcoming.

To install:
- Open a terminal window
- Create a directory and cd to that directory
- Copy json_from_xml.py and requirements.txt into that directory
- Run the following commands:
  - python3 -m venv env
  - source env/bin/activate
  - pip install --upgrade pip
  - pip install -r requirements.txt

Test the installation by running:
- python json_from_xml.py --help

This should display help information.

To convert an EML XML file:
- python json_from_xml.py [input file pathname]

The input file must have a .xml extension.

The output JSON file will have the same name as the input file, but with the .xml extension replaced by .json.

Whenever you run json_from_xml.py, you need first to activate the virtual environment created in the installation steps above.
I.e., do:
- Open a terminal window
- cd to the directory where you installed json_from_xml.py
- source env/bin/activate

You can now run json_from_xml.py


