import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

from jinja2 import Template

class ImgExtractor(Treeprocessor):
	def __init__(self, doc):
		self.md = doc
		self.md.images = []

	def run(self, doc):
		"Find all images and append to markdown.images"
		print('YO!!!!')
		for element in doc.iter():
			if element.tag == 'p':
				pass
				# self.md.images.append(element.text)
			elif element.tag == 'img':
				# element.set('width', '42')
				print(element)
				self.md.images.append(element.get('src'))

class ImgExtExtension(Extension):
	def extendMarkdown(self, md, md_globals):
		img_ext = ImgExtractor(md)
		md.treeprocessors.add('imgext', img_ext, '>inline')
		# md.treeprocessors.register(ImgExtractor(md), 'imgext', 15)

# foo = markdown.markdown(open('foo.md', 'r').read(), extensions=[ImgExtExtension()])
foo = markdown.Markdown(extensions=[ImgExtExtension()])
bar = foo.convert(open('foo.md', 'r').read())
print(foo.images)

template = Template(open('template.html').read())

f = open('site.html', 'w')

f.write(template.render(content=foo.images))

f.close()

# import boto3

# s3_client = boto3.client('s3')

# s3_client.upload_file('img1.jpg', 'expose-bucket', 'img1.jpg')
##s3 = boto.connect_s3()



