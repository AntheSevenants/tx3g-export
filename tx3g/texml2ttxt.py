from tx3g.texml import TeXML
from tx3g.txtt import TXTT

class TeXML2TXTT:
	def __init__(self, texml_path, txtt_path, txtt_out_path):
		texml = TeXML(texml_path)
		entry_values = texml.get_subtitle_entry_values()
		
		txtt = TXTT(txtt_path)
		txtt.substitute_subtitle_entry_values(entry_values)
		
		txtt.save(txtt_out_path)