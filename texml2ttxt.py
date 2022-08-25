import argparse

from tx3g.texml import TeXML

parser = argparse.ArgumentParser(description='Combine TeXML and TXTT files.')
parser.add_argument('texml_path', type=str, help='the path to your TeXML file')
parser.add_argument('txtt_path', type=str, help='the path to your input TXTT file')

args = parser.parse_args()

texml = TeXML(args.texml_path)
print(texml.get_subtitle_entry_values())