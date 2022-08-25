import argparse

from tx3g.texml import TeXML
from tx3g.txtt import TXTT

parser = argparse.ArgumentParser(description='Combine TeXML and TXTT files.')
parser.add_argument('texml_path', type=str, help='the path to your TeXML file')
parser.add_argument('txtt_path', type=str, help='the path to your input TXTT file')
parser.add_argument('txtt_out_path', type=str, help='the path to your output TXTT file')

args = parser.parse_args()

texml = TeXML(args.texml_path)
entry_values = texml.get_subtitle_entry_values()

txtt = TXTT(args.txtt_path)
txtt.substitute_subtitle_entry_values(entry_values)

txtt.save(args.txtt_out_path)