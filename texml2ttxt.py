import argparse

parser = argparse.ArgumentParser(description='Combine TeXML and TXTT files.')
parser.add_argument('texml_path', type=str, help='the path to your TeXML file')
parser.add_argument('txtt_path', type=str, help='the path to your input TXTT file')

args = parser.parse_args()
