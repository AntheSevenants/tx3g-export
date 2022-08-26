import argparse

from tx3g.texml2ttxt import TeXML2TXTT

parser = argparse.ArgumentParser(description='Combine TeXML and TXTT files.')
parser.add_argument('texml_path', type=str, help='the path to your TeXML file')
parser.add_argument('txtt_path', type=str, help='the path to your input TXTT file')
parser.add_argument('txtt_out_path', type=str, help='the path to your output TXTT file')

args = parser.parse_args()

TeXML2TXTT(args.texml_path, args.txtt_path, args.txtt_out_path)