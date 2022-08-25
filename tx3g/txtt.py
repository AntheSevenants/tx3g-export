from lxml import etree

class TXTT:
	def __init__(self, txtt_path):
		self.txtt_path = txtt_path

		with open(self.txtt_path, "rb") as reader:
			raw_text = reader.read()

		#raw_text = raw_text.decode("UTF-8")
		self.root = etree.fromstring(raw_text)

	def substitute_subtitle_entry_values(self, entry_values):
		text_sample_elements = self.root.xpath("//TextSample")

		#print(len(entry_values))
		#print(len(text_sample_elements))

		if len(entry_values) != len(text_sample_elements) - 1:
			raise Exception("Entry values count does not equal text sample element count")

		for index, text_sample_element in enumerate(text_sample_elements):
			if index == len(text_sample_elements) - 1:
				break

			text_sample_element.text = entry_values[index]

	def save(self, txtt_out_path):
		etree.ElementTree(self.root).write(txtt_out_path, pretty_print=True)