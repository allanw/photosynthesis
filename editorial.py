import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

from jinja2 import Template


import sys
if sys.platform == 'ios':
	import workflow
	import clipboard

class ImgExtractor(Treeprocessor):
	def __init__(self, doc):
		self.md = doc
		self.md.images = []
		self.md.text = []

	def run(self, doc):
		"Find all images and append to markdown.images"
		for element in doc.iter():
			if element.tag == 'p':
				if element.text:
					self.md.text.append(element.text)
			elif element.tag == 'img':
				# element.set('width', '42')
				self.md.images.append(element.get('src'))

class ImgExtExtension(Extension):
	def extendMarkdown(self, md, md_globals):
		img_ext = ImgExtractor(md)
		md.treeprocessors.add('imgext', img_ext, '>inline')
		# md.treeprocessors.register(ImgExtractor(md), 'imgext', 15)

# foo = markdown.markdown(open('foo.md', 'r').read(), extensions=[ImgExtExtension()])
foo = markdown.Markdown(extensions=[ImgExtExtension()])

if sys.platform == 'ios':
	mddoc = workflow.get_input()
	bar = foo.convert(mddoc)

	templatefile = clipboard.get()

	template = Template(templatefile)

	workflow.set_output(output)

	clipboard.set(output)
else:
	bar = foo.convert(open('foo.md', 'r').read())

	template = Template(open('template.html').read())

f = open('site.html', 'w')

output = template.render(content=zip(foo.images, foo.text))

f.write(output)

f.close()



# import boto3

# s3_client = boto3.client('s3')
# s3_client.upload_file('img1.jpg', 'expose-bucket', 'img1.jpg')
##s3 = boto.connect_s3()