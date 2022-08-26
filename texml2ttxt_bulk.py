import argparse
import os
from pathlib import Path

from tx3g.texml2ttxt import TeXML2TTXT

parser = argparse.ArgumentParser(description='Combine TeXML and TTXT files.')
parser.add_argument('texml_dir_path', type=str, help='the path to your TeXML files')
parser.add_argument('ttxt_dir_path', type=str, help='the path to your input TTXT files')
parser.add_argument('ttxt_out_dir_path', type=str, help='the path to your output TTXT files')

args = parser.parse_args()

texml_paths = os.listdir(args.texml_dir_path)
for texml_path in texml_paths:
	# Skip gitignore
	if texml_path[0] == ".":
		continue

	no_ext_path = Path(texml_path).stem

	texml_path = f"{args.texml_dir_path}/{texml_path}"
	ttxt_path = f"{args.ttxt_dir_path}/{no_ext_path}.ttxt"
	ttxt_out_path = f"{args.ttxt_out_dir_path}/{no_ext_path}.ttxt"

	if not os.path.exists(ttxt_path):
		raise FileNotFoundError(f"Corresponding TTXT for {no_ext_path} does not exist. Do they have equal base names?")

	TeXML2TTXT(texml_path, ttxt_path, ttxt_out_path)