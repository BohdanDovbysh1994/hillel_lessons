# import xml.etree.ElementTree as ET
# import re
#
# tree = ET.parse('example.xml')
# root = tree.getroot()
# root_attr = root.attrib

# for child in root:
#     print(child.tag, child.attrib)

# print([elem.tag for elem in root.iter()])

# print(ET.tostring(root, encoding='utf8').decode('utf8'))

# for decade in root.iter('decade'):
#     if decade.attrib['years'] == '1980s':
#         for child in decade:
#             print(child.tag, child.attrib['title'])


# def get_movie_by_year(xml_document, year):
#     tree = ET.parse(xml_document)
#     root = tree.getroot()
#     for decade in root.iter('decade'):
#         if decade.attrib['years'] == f'{year}s':
#             for child in decade:
#                 print(child.tag, child.attrib['title'], decade.attrib['years'])
#
#
# get_movie_by_year('example.xml', 1980)

# print description
# for description in root.iter('description'):
#     print(description.text)

# XML Xpath example
# for movie in root.findall("./genre/decade/movie/[rating='R']"):
#     print(movie.attrib)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
#     attr = movie.attrib
#     print(movie.attrib)

# for movie in root.findall("./genre/decade/movie/format[@multiple='Yes'].../../..."):
#     print(movie.attrib)

# b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
# b2tf.attrib['title'] = 'Back TEST the Future'
#
# tree.write("example.xml")
# print(b2tf)
#
# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

# for form in root.findall("./genre/decade/movie/format"):
#     # Search for the commas in the format text
#     match = re.search(',', form.text)
#     if match:
#         form.set('multiple', 'Yes')
#     else:
#         form.set('multiple', 'No')

# Write out the tree to the file again
# tree.write("example.xml")
#
# tree = ET.parse('example.xml')
# root = tree.getroot()
#
# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

import Movie

Movie().from_xml()