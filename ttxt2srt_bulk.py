import argparse
import subprocess
import os
from pathlib import Path

from tx3g.texml2ttxt import TeXML2TTXT

parser = argparse.ArgumentParser(description='Convert TTXT files to SRT (uses mp4box).')
parser.add_argument('ttxt_dir_path', type=str, help='the path to your TTXT files which you want to convert to SRT')
parser.add_argument('srt_out_dir_path', type=str, help='the path to your output SRT files')

args = parser.parse_args()

ttxt_paths = os.listdir(args.ttxt_dir_path)
for ttxt_path in ttxt_paths:
	# Skip gitignore
	if ttxt_path[0] == ".":
		continue

	no_ext_path = Path(ttxt_path).stem

	ttxt_path = f"{args.ttxt_dir_path}/{ttxt_path}"
	srt_path = f"{args.srt_out_dir_path}/{no_ext_path}.srt"

	subprocess.Popen(["mp4box", "-srt", ttxt_path, "-out", srt_path])