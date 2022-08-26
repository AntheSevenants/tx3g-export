import argparse

from tx3g.texml2ttxt import TeXML2TTXT

parser = argparse.ArgumentParser(description='Combine TeXML and TTXT files.')
parser.add_argument('texml_path', type=str, help='the path to your TeXML file')
parser.add_argument('ttxt_path', type=str, help='the path to your input TTXT file')
parser.add_argument('ttxt_out_path', type=str, help='the path to your output TTXT file')

args = parser.parse_args()

TeXML2TTXT(args.texml_path, args.ttxt_path, args.ttxt_out_path)