from lxml import etree

class TeXML:
	def __init__(self, texml_path):
		with open(texml_path, "rb") as reader:
			raw_text = reader.read()

		raw_text = raw_text.decode("UTF-8")
		self.root = etree.fromstring(raw_text)

	def get_subtitle_entry_values(self):
		text_elements = self.root.xpath('//text')

		entry_values = [ text_element.text for text_element in text_elements ]

		return entry_values